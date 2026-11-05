# Internal acceptance and publishing record

# Systems Engineering Library — Acceptance and Usability Review

The library's learner-facing naming and navigation have been standardized. The full curriculum remains present, and the reference system is organized around learning rather than publication history.

## Learner experience

- The homepage, encyclopedia, learning routes, A–Z references, study desk, book readers and course navigation use stable learner-facing names.
- Release numbers and packaging labels have been removed from visible HTML page content, including legacy introductory pages and canonical reference labels.
- The two older entry pages now direct readers to the current encyclopedia, learning routes, textbooks, and labs instead of describing the library as a prototype.
- A new [Offline Reading Help](SE/K/OFFLINE-HELP.html) page explains extraction, how study markers work, and what to do when a browser restricts local file functionality.
- The 56 canonical reference Markdown sources were synchronized with their cleaned HTML presentation. Engineering examples and citation provenance were retained.

## Acceptance evidence

| Check | Result |
|---|---|
| HTML pages inspected | 1,270 |
| Relative local links/assets checked | 23,197 |
| Missing local file targets | 0 |
| Fragment references checked | 2,793 |
| Standard HTML fragment problems | 0 |
| Dynamic lab-catalog paths checked | 260 / 260, all found in 810 catalog records |
| Indexed learning resources | 1,076, all IDs unique |
| Canonical references | 56 |
| Original files retained byte-for-byte | 3,024 |
| Original files updated | 152, restricted to interface HTML and reference/entry Markdown metadata |
| Original files removed | 0 |
| Browser interaction checks | 16 / 16 passed |
| Simulated cross-page study-marker checks | 4 / 4 passed |
| Learner-visible release-version labels in HTML | 0 found by the defined search |

Search by engineering question, reference reading, returning to search results, A–Z browsing, opening guided routes, narrow-viewport display, the homepage, standalone navigation, and study-desk rendering were checked using Chromium with inlined local assets. The simulated cross-page storage tests confirmed that saving and marking a chapter studied showed up in the study desk and homepage.

## Scope and remaining limitations

**Native extracted-folder acceptance on Windows remains unverified.** The available Chromium environment blocks direct navigation to local `file://` and localhost addresses, including with local route interception. For interactive checks, pages and local scripts were loaded directly into Chromium. Link and lab-catalog integrity were checked separately against the extracted files. The browser-state persistence check used a shared test storage shim; it does not prove that native local-file storage will persist on a particular Windows browser.

No external user sessions, NVDA/VoiceOver screen-reader sessions, or independent review of textbook mathematics were completed. The internal Windows acceptance checklist lists steps to carry out on a Windows computer before asserting production cross-browser compatibility.

## Getting started

Extract the ZIP and open `SE/START-HERE.html`. The downloaded file and learner interface are titled **Systems Engineering Library**. The instructional content and coursework do not require a login.
