# Spec Delta

## Purpose

Resolve a flow target and render its Mermaid content to HTML via Pele, then
display it in vocus, so flow artifacts are viewable without a browser.

## ADDED Requirements

### Requirement: Resolve flow target
The system SHALL resolve a flow target from a file path, directory, or topic
slug (mirroring mdview's resolution).

#### Scenario: File path
- **WHEN** a path to a .md or .mmd file is given
- **THEN** that file is used as the flow source

#### Scenario: Topic slug
- **WHEN** a topic slug is given
- **THEN** the first .md/.mmd under topics/<slug> is used

### Requirement: Render Mermaid to HTML
The system SHALL convert Mermaid fenced blocks (or raw .mmd) into HTML that
loads Pele from CDN and calls pele.mount on each pre.mermaid element.

#### Scenario: Markdown with mermaid fence
- **WHEN** input contains a ```mermaid fenced block
- **THEN** output HTML contains a pre.mermaid element with the diagram source
  and the Pele CDN script

#### Scenario: Raw .mmd
- **WHEN** input is a raw .mmd file
- **THEN** the entire content is wrapped as a single pre.mermaid element

### Requirement: View in vocus
The system SHALL pipe the rendered HTML to vocus with an appropriate title.

#### Scenario: Successful render
- **WHEN** rendering succeeds
- **THEN** vocus opens displaying the diagram

### Requirement: Handle Pele errors
The system SHALL surface Pele render errors as text (via PeleError) in the
rendered page rather than crashing.

#### Scenario: Invalid diagram
- **WHEN** the Mermaid source is invalid
- **THEN** the page shows the error message text