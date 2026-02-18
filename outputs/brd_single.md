# Business Requirements Document (BRD) – R&D Sensory UX Data Platform Phase 2

# 0. Header Information

| Field | Value |
| --- | --- |
| Project Name | R&D Sensory UX Data Platform – Phase 2 Enhancements |
| Date | 2025-05-30 |
| Status | Draft for Review |
| Document Owner | Angela Li (R&D Sensory), Jenn Soong (Data Admin) |
| Version | 0.1 |

# 1. Executive Summary

- Purpose: Enhance the existing R&D Sensory UX application and data pipeline to improve efficiency, data quality, and usability for sensory and analytical testing.
- What is being built: Phase 2 improvements to workflows (pre-approval, editing controls), vendor and internal portals, data transformation engine accuracy, UI/UX, and data quality validations; support for non‑product projects; reporting enhancements.
- Who benefits: Sensory UX leads, R&D leads, line managers, sensory directors, analytical team members, external accredited sensory agencies (vendors), and data/BI teams.
- Intended outcomes: Faster turnaround from test initiation to insight; reduced manual rework; improved data integrity; better collaboration and approvals; scalable global usage.
- Context: Current system live since early March 2025 with ~45 incidents resolved/stabilizing; app supports global users and external vendors; Power BI reporting consumes curated sensory schema tables.
- Key priorities: Improve AI-based transformation matching accuracy, add pre‑RFP approval, allow post‑completion admin edits to data with governance, enable multi‑editor collaboration, better UX and data exports.

# 2. Business Context & Problem Statement

- Background / context:
  - Custom Power Apps solution with three components: Stakeholder portal (internal), Vendor portal (external), and a data transformation module feeding SQL and Power BI.
  - Data sources include sensory testing (consumer surveys and descriptive analysis) and analytical instrument measures; ~94% of overall data volume is sensory.
  - Internal SQL database with initial ~19 sensory tables; total ~35 tables after app additions (R&D schema for app functions, sensory schema for curated reporting).
- Current state (if stated):
  - Go-live early March 2025; initial hypercare complete; now on basic incident support (1 Power Apps developer, 1 Python engineer from vendor).
  - Reactive incident management (~45 tracked in Excel) with stabilization over three months; usage inferred via active tests rather than formal telemetry.
  - Power BI reports consume sensory schema data once tests are concluded (holding/app tables push to sensory tables post-completion).
- Problem / pain points:
  - Transformation engine matching accuracy significantly below promised (often ~65% vs claimed 95%); supervised improvement not materializing.
  - UX friction: heavy horizontal/vertical scrolling; poor visibility of uploaded files; limited search/filter; clunky admin for large lookups (700+ questions, 500+ attributes).
  - Workflow gaps: no pre‑RFP approval; inability to edit data after test completion (changes don’t propagate to sensory schema); single‑editor constraint; SIF lacks bulk copy/paste and export.
  - Data quality issues: inconsistent values (blank/NA variants), duplicate entries due to uncontrolled dropdowns and validation gaps.
  - Security/observability gaps: no confirmed performance/security testing or proactive availability monitoring despite external vendor access.
- Why now / business drivers:
  - Accelerate data-driven product insights and set foundation for future predictive analytics (formulation/process/material attributes integration).
  - Reduce manual rework and admin overhead for data admins and leads; improve global vendor collaboration and reporting fidelity.

# 3. Objectives & Success Metrics

- Objectives:
  - Increase transformation engine mapping accuracy and reduce manual review effort.
  - Introduce pre‑RFP approval and governance to prevent downstream rework.
  - Enable post‑completion admin edits that propagate to curated tables with auditability.
  - Improve UX (navigation, visibility, search/filter) and enable multi‑editor collaboration.
  - Strengthen data quality validations and dropdown controls; support non‑product projects.
  - Establish basic performance/security/availability baselines for an app with external access.
- Success metrics / KPIs (where available):
  - Transformation matching accuracy improved from observed ~65% to a higher defined threshold (target to be confirmed).
  - Reduction in incident volume from initial ~45 (tracked) and decrease in recurring incidents (baseline tracked in Excel).
  - Time to create SIF and process data reduced (baseline not stated; to be measured).
  - Go-live stability for Phase 2 features without material increase in incidents.
- Baseline (if stated):
  - Transformation matching observed as low as ~65% for some studies; ~45 incidents logged post-launch.
- Measurement cadence & owners (if stated):
  - Not specified; current tracking is ad hoc (Excel). Owners: Data Admins (Angela, Jenn).

# 4. Scope

| In Scope (4.1) | Out of Scope (4.2) |
| --- | --- |
| Pre‑RFP approval workflow for sensory tests | Building a net-new predictive analytics application |
| Admin post‑completion data edits that update sensory schema | Full integration with SAP/Coupa vendor master and PO systems (Phase 3/future) |
| UX improvements: navigation, reduced scrolling, visibility of uploads, improved search/filter | Major re-platforming away from Power Apps |
| SIF bulk copy/paste and export (Excel/PDF) | Vendor master data stewardship beyond application needs |
| Multi‑editor collaboration on active tests | Rewriting existing reporting stack in non-Power BI tools |
| Transformation engine accuracy and supervised matching enhancements |  |
| Data quality validations and dropdown category controls |  |
| Support for non‑product projects (no SIF) |  |
| Conclude-test gate linked to data transformation completion |  |
| Study name–project number automation with admin approval workflow |  |

- 4.3 Constraints (only what is stated):
  - Power Apps UX limitations cited by vendor; timeline/resource constraints impacted initial UX scope.
  - External vendors require separate IDs and licenses; internal additions require platform team action.
  - Support resources are scoped for incidents only, not enhancements.
  - Data pushed to sensory schema only after test completion (current design).

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Create RFP; manage vendor interactions; prepare one-pager; submit reports; conclude tests | Access to own tests and peers’ completed tests |  |
| R&D Lead | Complete Sample Information Form (SIF); micro clearance acknowledgments | Access to assigned tests/SIF |  |
| Line Manager | Approve one-pager/proposals; review final reports | Approval views; limited scope currently | Requested capability to complete full test workflow if they oversee testing |
| Sensory Director | Approve one-pager/proposals; review final reports | Approval views |  |
| Analytical Lead | Create internal analytical tests; upload instrument data | No approvals in analytical workflow |  |
| Data Admin (e.g., Angela, Jenn) | Administer users/vendors/dropdowns; bypass approvals; manage transformation reviews; manage categories; maintain data | Admin view of all tests; app admin features | Seek post-completion edit capabilities and automation |
| Vendor (External Agency) | View RFP details and SIF; submit proposals, raw data, and reports; enter sample codes and equipment | Vendor portal with limited access | Separate authentication (email-based); license required |
| Platform Team (e.g., Kaushal) | Provision licenses/access for internal/external users | N/A | Must be notified for user provisioning |
| Support Engineers (Vendor) | Incident support only: Power Apps developer and Python engineer for transformation | N/A | Not currently chartered for enhancements |

# 6. Functional Requirements

1. [Pre‑RFP & Approvals] FR-1: The system shall provide a pre‑RFP approval step where Sensory UX Leads can submit a one‑pager to Line Manager and Sensory Director for approval prior to sending any RFP to vendors.
2. [Pre‑RFP & Approvals] FR-2: The system shall allow approvers to approve or request changes on the pre‑RFP one‑pager with comments and return to the Sensory UX Lead.
3. [Pre‑RFP & Approvals] FR-3: Upon approval of the pre‑RFP one‑pager, the system shall lock approved fields (as configured) and prefill them into the RFP sent to vendors.
4. [Vendor Portal] FR-4: The system shall allow vendors to view RFP details and submit proposals; multiple vendor proposals per RFP shall be supported.
5. [Vendor Portal] FR-5: The system shall notify Sensory UX Leads via email upon each vendor submission and status change.
6. [Approvals] FR-6: The system shall support line manager and director approvals for proposals/one‑pager and final report with the ability to send back for changes.
7. [Test Creation] FR-7: Upon proposal approval, the system shall create a Test ID and transition to the test execution phase.
8. [SIF] FR-8: R&D Leads shall be able to complete and submit the Sample Information Form (SIF), including product info, cooking instructions, holding/delivery protocol, and equipment details.
9. [SIF] FR-9: Vendors shall be able to enter per-sample codes (blinding/labels) and verify lot codes within the SIF view.
10. [SIF] FR-10: The system shall provide bulk copy/paste for SIF data entry across multiple samples.
11. [SIF] FR-11: The system shall provide SIF export to Excel and/or PDF.
12. [SIF Dropdowns] FR-12: The system shall restrict dropdown options by category (e.g., primary package types show only primary; exclude secondary/delivery types).
13. [Micro Clearance] FR-13: The system shall support micro clearance acknowledgments for pilot-line samples, captured by R&D Leads.
14. [Vendor Files] FR-14: Vendors shall be able to upload raw data and reports to designated sections per test.
15. [Admin – Vendors/Users] FR-15: Admins shall be able to manage vendor profiles and internal stakeholders, with triggers to notify the platform team for license/access provisioning.
16. [Admin – Dropdowns] FR-16: Admins shall be able to manage dropdown lists (including three-level dependent lists such as country/region) via an interface, with bulk update support.
17. [Admin – Bypass] FR-17: Admins shall be able to bypass specific approval steps when approvers are unavailable, with audit trail.
18. [Data Transformation] FR-18: The system shall ingest vendor raw data into an intermediate file where mapping to canonical question IDs is proposed with match scores.
19. [Data Transformation] FR-19: Data Admins shall be able to review intermediate mappings, annotate (remove/mismatch/new) and upload corrected intermediate files.
20. [Data Transformation] FR-20: The system shall generate an output file restructured for database ingestion (e.g., respondent-level stacked responses) and load it to curated tables upon test completion.
21. [Transformation Accuracy] FR-21: The system shall provide configurable match score thresholds and surface low-confidence mappings for manual review.
22. [Conclude Test Gate] FR-22: The system shall prevent test conclusion until Data Admins confirm data transformation completion for that test (or allow admin override with justification).
23. [Post‑Completion Edits] FR-23: Admins shall be able to edit select fields and raw data after test completion, with those changes propagating to the sensory schema and being fully audited.
24. [Collaboration] FR-24: The system shall allow multiple assigned editors (e.g., multiple sensory team members) to work on active tests with conflict handling rules (e.g., field-level locking or last-writer-wins with change log).
25. [Non‑Product Projects] FR-25: The system shall allow creation and tracking of projects that do not require a SIF (non‑product testing), without breaking workflow or reporting.
26. [Study–Project Automation] FR-26: The system shall auto-populate valid Study Names based on an entered Project Number; if a Project Number is new, a request shall be routed to Admin for approval to add Study Name.
27. [Reporting] FR-27: The system shall enable improved search and filter for completed tests (e.g., by region, test type, product) and provide visibility of which files are uploaded per section.
28. [Document Generation] FR-28: The system shall generate a downloadable one‑pager (PowerPoint) populated from RFP/one‑pager fields.
29. [Document Generation] FR-29: The system shall generate a McCain report template (PowerPoint) populated from test fields where defined.
30. [Notifications] FR-30: The system shall send email notifications for key events (vendor submissions, approvals, SIF assignments, transformation review requests, conclusion readiness).
31. [Security & Access] FR-31: The system shall authenticate external vendors using separate email-based credentials and restrict access strictly to their projects.
32. [Security & Access] FR-32: The system shall authenticate internal users via the company directory and role-based access (view/edit limited to own tests and peers’ completed tests unless admin).

# 7. Non-Functional Requirements (NFRs)

- Performance:
  - NFR-1: The system shall maintain acceptable response times under concurrent usage by global users (specific targets TBD).
  - NFR-2: The data transformation process shall complete within a reasonable time window for typical study files (target TBD based on current volumes).
- Security & Access:
  - NFR-3: The system shall segregate external vendor identities from internal directory users and enforce least-privilege access.
  - NFR-4: The system shall undergo security testing appropriate for external access (e.g., vulnerability assessment) prior to Phase 2 release.
- Availability & Reliability:
  - NFR-5: Basic availability monitoring (URL health checks) and alerting shall be established for the application.
  - NFR-6: Incident handling processes shall remain in place with defined escalation paths.
- Usability & UX:
  - NFR-7: UI shall minimize horizontal/vertical scrolling and clearly indicate uploaded file presence and status.
  - NFR-8: Admin tools shall support bulk management of large reference lists (e.g., 700+ questions, 500+ attributes).
- Auditability & Logging:
  - NFR-9: All post‑completion data edits and approval bypasses shall be logged with user, timestamp, and change details.
- Compliance & Privacy:
  - NFR-10: The system shall handle respondent and vendor data in accordance with corporate privacy and data handling policies (details TBD).
- Data Quality:
  - NFR-11: The system shall validate and standardize common values (e.g., normalize blanks/NA) to prevent duplicates before writing to SQL.
  - NFR-12: Dropdowns shall be category-filtered to avoid invalid selections and reduce data inconsistency.

# 8. Data Requirements

- 8.1 Entities / Objects (if stated):
  - Proposal, Test, Vendor, Sample, SIF (product info, cooking, holding/delivery, equipment), Micro Clearance, Vendor Files (raw data, reports), McCain Report, Question, Attribute, Respondent, Product, Equipment, Packaging Types, Category Mapping, Study, Project Number, Budget/PO info, Notifications, Users/Roles.
- 8.2 Key fields & validations (if stated):
  - Project Number ↔ Study Name mapping (auto-populate; admin approval for new).
  - Product fields (SKU, lot code, product type) mandatory for SIF where applicable.
  - Dropdown category enforcement (e.g., primary vs secondary vs delivery packaging types).
  - Validation to standardize blanks/NA and prevent duplicate entries.
- 8.3 Data quality rules (if stated):
  - Normalize common nulls (blank, NA, N/A) to a single representation.
  - Deduplicate entries where semantically identical values are detected.
  - Enforce allowed lists per category; flag out-of-domain values.
  - Log all post-completion edits and ensure propagation to sensory schema.

# 9. Integrations & Interfaces

- Systems involved:
  - Power Apps (stakeholder and vendor portals), SQL Database (R&D and Sensory schemas), Power BI (reporting).
- Direction / triggers / frequency (if stated):
  - Transformation engine ingests vendor files to intermediate/output then writes to SQL; curated sensory tables populated post-test completion.
  - Email notifications triggered on submissions, approvals, assignments, and readiness to conclude.
  - Future (not in Phase 2): SAP/Coupa vendor master, PO/budget linkages.
- Error handling expectations (if stated):
  - Intermediate review loop for low-confidence mappings; manual corrections by Data Admins prior to final load.

# 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Power BI reports showing tested products, results, counts of tests by region/test type, and improved filters for completed tests.
- Filters/dimensions:
  - Region, test type (sensory vs analytical), product, status; additional filters as feasible.
- Intended users:
  - Sensory UX leads, R&D leads, line managers, sensory directors, analytical leads, data team.

# 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - Not defined; incident response currently handled by vendor support resources.
- Operational ownership/support model (if stated):
  - Vendor provides incident support: 1 Power Apps developer and 1 Python engineer for transformation; enhancements excluded from support scope.
  - Reactive monitoring via user-reported issues; no formal observability tooling in place (to be addressed).

# 12. Risks, Dependencies, and Assumptions

- Risks:
  - Transformation matching accuracy remains below target; supervised improvement not implemented as promised.
  - UX limitations reduce adoption efficiency; increased training and support load.
  - Lack of performance/security testing despite external access.
  - Post‑completion data immutability currently blocks corrections; risk of data discrepancies in curated tables.
- Dependencies:
  - Platform team (licensing/access provisioning for internal/external users).
  - Vendor support for Power Apps and Python transformation module.
  - Future SAP/Coupa integrations (Phase 3/future) dependent on corporate programs.
- Assumptions:
  - None stated beyond the provided inputs.

# 13. Timeline & Milestones

| Milestone | Date/Window | Notes |
| --- | --- | --- |
| Requirements (initial SOL) | Late Sep–Oct 2024 | Initial requirements finalized; development began October 2024 |
| Initial Go‑Live | Early March 2025 | Live Feb; official early March 2025 |
| Hypercare | March 2025 | High incident volume initially; stabilized over time |
| Phase 2 Estimation | Week of 2025-06-02 (target) | Rough order-of-magnitude estimate requested by Angela |
| Phase 2 Delivery Window (indicative) | 3–6 months (TBD) | Parallelizable UX and workflow items; specifics to be planned |

# 14. Open Questions (to finalize BRD)

- What is the target transformation matching accuracy threshold (e.g., % exact/acceptable matches) and how will supervised learning be implemented/validated?
- Which fields should be locked by pre‑RFP approval and which remain editable without re‑approval?
- Scope and governance for post‑completion edits: which roles, which fields, and required approvals (if any)?
- Collaboration rules for multi‑editor editing (conflict resolution approach, field-level locking vs. change log).
- Specific performance and availability targets (e.g., response times, uptime) and monitoring tools to be used.
- Security testing scope and ownership (vulnerability assessment, pen test, frequency) given external vendor access.
- Exact filters and search dimensions required for completed test views and Power BI.
- Detailed definition of non‑product project types and minimal required fields/workflow steps.
- Study Name–Project Number rules (one-to-one vs one-to-many) and approval SLAs for adding new mappings.
- Final list of SIF dropdown categories and allowed values per category (primary/secondary/delivery types).
- User base forecast: confirm expected active users within a year (50–100 vs other growth projections) to size performance testing.
- Document generation templates: confirm PowerPoint templates and fields for one‑pager and McCain report.

# 15. Source Notes

- Primary notes used: INPUTS_TEXT (RnD Sensory - Roadmap Discussion, 2025-05-30 meeting transcript).
- Brownfield notes used: None provided.