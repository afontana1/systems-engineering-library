"""Model-based architecture graph checks. Syntactic checks are not semantic assurance."""
from __future__ import annotations
from collections import defaultdict
import json
from pathlib import Path


def load_model(file):
    return json.loads(Path(file).read_text(encoding='utf-8'))


def validate_model(model):
    errors = []
    components = model.get('components', [])
    interfaces = model.get('interfaces', [])
    requirements = model.get('requirements', [])
    hazards = model.get('hazards', [])
    def validate_unique(items, kind):
        ids = [item.get('id') for item in items]
        if any(not x for x in ids) or len(ids) != len(set(ids)):
            errors.append(f'{kind}: blank or duplicate identifier')
        return set(ids)
    cids = validate_unique(components, 'components')
    iids = validate_unique(interfaces, 'interfaces')
    rids = validate_unique(requirements, 'requirements')
    hids = validate_unique(hazards, 'hazards')
    allowed_states = {'received', 'queued', 'assigned', 'completed', 'unserved', 'rejected'}
    for i in interfaces:
        for key in ('from', 'to'):
            if i.get(key) not in cids:
                errors.append(f"{i.get('id')}: unknown {key} endpoint {i.get(key)}")
        if not i.get('schema') or not i.get('failure_handling'):
            errors.append(f"{i.get('id')}: missing contract or failure handling")
        if i.get('from') == i.get('to'):
            errors.append(f"{i.get('id')}: self-loop requires explicit decomposition")
    for r in requirements:
        if r.get('allocated_to') not in cids:
            errors.append(f"{r.get('id')}: invalid allocation")
        if not r.get('verification_id'):
            errors.append(f"{r.get('id')}: no verification linkage")
        if not r.get('acceptance'):
            errors.append(f"{r.get('id')}: no acceptance criterion")
    for h in hazards:
        if h.get('control_component') not in cids:
            errors.append(f"{h.get('id')}: unknown control component")
        if not h.get('test_id'):
            errors.append(f"{h.get('id')}: no linked test")
    transition_graph = defaultdict(set)
    for t in model.get('transitions', []):
        if t.get('from') not in allowed_states or t.get('to') not in allowed_states:
            errors.append('illegal transition state')
        transition_graph[t.get('from')].add(t.get('to'))
    if 'queued' not in transition_graph['received'] or 'assigned' not in transition_graph['queued']:
        errors.append('required request lifecycle edges missing')
    if not any(x.get('id') == 'Dispatcher' for x in components):
        errors.append('missing Dispatcher')
    return {'valid': not errors, 'errors': errors,
            'component_count': len(components), 'interface_count': len(interfaces),
            'requirements_count': len(requirements), 'hazards_count': len(hazards),
            'caveat': 'Graph syntax, topology, and declared links checked; behavior and engineering claims need separate review'}
