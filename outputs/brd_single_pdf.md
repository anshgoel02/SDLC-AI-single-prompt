# BRD: R&D Sensory UX Data Platform (Current State and Phase 2 Enhancements)

# # 0. Header Information

- Project Name: R&D Sensory UX Data Platform (Stakeholder & Vendor Portals, Transformation Engine, Power BI)
- Date: 2025-05-30
- Status: In production (Mar 2025 go-live); planning Phase 2 enhancements
- Document Owner: R&D Sensory UX / Data Admin (Angela Li, Jenn Soong)
- Version: 1.0 (Initial BRD from roadmap discussion and workflow doc)

# # 1. Executive Summary

- Purpose: Centralize sensory (human perception) and analytical (instrument) test workflows and data to drive efficient, accurate product and consumer insights.
- What is being built: A Power Apps-based Stakeholder Portal, Vendor Portal, and Data Transformation Engine feeding a SQL database (sensory and R&D schemas) and Power BI reports; Phase 2 to address UX, data quality, and workflow gaps.
- Who benefits: Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Analytical Leads, Data Admins, and external accredited sensory agencies (vendors).
- Intended outcomes: Faster approvals and test setup, standardized data capture, reduced manual effort validating vendor data, searchable historical insights, and readiness for future predictive analytics.
- Current coverage: Majority of database is sensory data (≈94% of total); analytical data captured with a lighter workflow (no approvals).
- Phase 2 focus: Pre-RFP approvals, DA edit rights post-completion with propagation to reporting tables, improved UX and search/export, gating completion until transformation done, better dropdown logic and data standardization, multi-collaboration, and support for non-product tests.

# # 2. Business Context & Problem Statement

- Background/context:
  - R&D Sensory UX team collaborates with Product Development and Marketing; majority of sensory tests are run by external accredited agencies (consumer tests and descriptive analysis).
  - App in production since early Mar 2025; built in ~4.5 months (requirements finalized Oct; intensive changes through Feb).
- Current state (if stated):
  - Stakeholder Portal for internal roles; Vendor Portal for external agencies; Data Transformation Engine to normalize vendor submissions; Power BI reporting on sensory schema.
  - Internal users authenticate via McCain AAD; vendors use separate email-based credentials provisioned by R&D with platform team support.
- Problem / pain points:
  - Historical sensory data previously transactional/hard to trend; app resolves structure but UX remains poor (excessive scrolling, unclear file link visibility).
  - Data transformation matching quality inconsistent; manual verification (remove/mismatch/new) is time-consuming; promised learning/improvement is not occurring.
  - Limited admin capabilities in-app (resort to SQL/Excel for bulk list management and study mapping).
  - Workflow gaps (no pre-RFP approval, cannot accommodate non-product tests without SIF, only one assignee can edit active tests, DA cannot edit data after completion with propagation).
- Why now / business drivers:
  - Need for efficient, accurate insight generation and a foundation for predictive analytics (longer-term: incorporate product information, materials, process parameters).
  - Stabilized core functions post go-live; Phase 2 required to address usability, data quality, and governance gaps and to reduce admin burden.

# # 3. Objectives & Success Metrics

- Objectives:
  - Streamline sensory and analytical workflows from RFP to completion with robust approvals and notifications.
  - Standardize vendor data ingestion with improved matching and reduced manual intervention.
  - Enhance UX to reduce time-on-task (search, filter, export, bulk input).
  - Strengthen governance (pre-RFP approvals, gating completion until transformation done, DA edit rights with propagation).
- Success metrics / KPIs (where measurable intent is stated):
  - Reduce manual verification effort for transformation mapping (baseline high; target reduction to be defined).
  - Decrease incident volume from hypercare levels (≈45 tracked incidents historically) to a stable low rate.
  - Improve discoverability/searchability of completed tests and artifacts (qualitative user feedback).
- Baseline (if stated):
  - Initial months saw daily incidents and recurring issues; now stabilized for basic functions after ~3 months in production.
  - Matching rates observed as low as ~65% in worst cases; promised learning not realized.
- Measurement cadence & owners (if stated):
  - Operationally tracked by Data Admins (Angela/Jenn) via incident log and active/completed test dashboards; usage approximated by active tests and role assignments.

# # 4. Scope

# ## 4.1 In Scope

- Current capabilities:
  - Stakeholder Portal (Sensory UX, LM, SD, R&D Lead, Analytical Lead, Data Admin) with dashboards, RFP creation, approvals, test creation, SIF, Micro Clearance, vendor data/report intake, and completion.
  - Vendor Portal for proposal submission, SIF completion (codes/equipment/packaging), raw data and report uploads, with notifications.
  - Data Transformation Engine with intermediate file review, mapping to reference questions/attributes, comments (remove/mismatch/new), and output file generation for ingestion to sensory schema.
  - Power BI reporting on sensory schema for tests, products, results; filters by region/test type (where implemented).
  - Admin functions: manage vendors (with license provisioning by platform team), manage dropdowns (including dependent lists), bypass approvals, manage reference lists, manage transformation engine, role/access management.
  - Notifications via Power Automate (e.g., vendor submissions, approvals, PO reminder).
  - Files stored in McCain Enterprise Data Platform/SharePoint test folders.
- Phase 2 enhancements (prioritized):
  - Pre-approval step before sending RFPs to vendors (LM/SD alignment).
  - Allow DA to edit data after test completion and propagate changes to reporting (sensory schema) with appropriate governance/audit.
  - UX improvements: minimize scrolling, clearer file/link visibility, improved search/filter for completed tests, one-pager download, PPT generation from entered fields.
  - Bulk copy/paste and export (Excel/PDF) for Sample Information Form (SIF); better dropdown category differentiation.
  - Gating test completion until Data Admin confirms transformation is complete; add reminder/validation.
  - Data standardization on input (handle blanks/NA, prevent duplicates).
  - Multi-collaborator editing on active tests; expand LM capability to complete full test workflow when needed.
  - Support for non-product testing projects without requiring SIF.
  - Auto-population of Study Name based on Project Number, with admin oversight/approval for new entries.

# ## 4.2 Out of Scope

- Predictive analytics and formulation prediction (future ambition).
- Integration with SAP/Coupa for PO/budget or vendor master (considered Phase 3/future).
- Supplier ingredient/spec management via TraceGains or similar (future/third-party).
- End-to-end observability tooling and automated performance/security testing (status to be clarified; not delivered in current scope).

# ## 4.3 Constraints (only what is stated)

- Platform constraints in Power Apps impacted UX flexibility (layout/visibility changes limited by vendor team and timelines).
- External vendors require licensed access; provisioning coordinated with platform team (Kaushal).
- Support resources from vendor (Power Apps, Python) focus on incidents only; enhancements routed to Phase 2.
- Multiple vendor data formats necessitate transformation engine; full standardization at source not feasible.

# # 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead (SL) | Initiate RFP, select vendors, create 1-Pager, manage SIF flow, create McCain report, conclude tests | Own tests + peers' completed; dashboards; vendor comms; upload/report views | Primary owner of sensory workflow |
| Line Manager (LM) | Approve 1-Pager and final reports; can initiate workflows | Dashboard for notifications, active/completed tests | May need capability to complete full workflow (Phase 2) |
| Sensory Director (SD) | Approve 1-Pager and final reports | Dashboard for notifications, active/completed tests | Approval authority; can comment/request changes |
| R&D Lead | Complete SIF (product details, cooking/holding), Micro Clearance acknowledgement | SIF & Micro Clearance lists linked by TestID | Provides sample prep details; submits to SL |
| Analytical Lead | Create analytical tests, assign R&D Lead, upload raw analytical data (basic validation) | Analytical dashboards (active/completed) | No approvals in analytical workflow |
| Data Admin (DA) | Manage vendors/dropdowns/reference lists, oversee transformation engine, verify question mapping, bypass approvals, manage roles | Admin view/edit all active/completed tests; access/download raw data | Also handle SQL/Excel for bulk list and study mapping until improved |
| Vendors (External) | Submit proposals, complete SIF parts (codes/equipment/packaging), upload raw data and reports | Vendor portal; limited visibility to proposal/SIF details; notifications | Authenticate with separate email-based credentials; licensed |
| Platform Team (Kaushal) | Provision user/vendor access/licenses | N/A | Email-based requests from Data Admins |
| BlackStraw Support (Power Apps: Azure; Python: Rahul; CRM: Subhanil) | Incident support only (app and transformation layer) | N/A | Enhancements routed to Phase 2; hypercare ended |
| IT/Analytics (Deepak Sharma, Preeti, Siddharth) | Assessment of Phase 2 scope, security/performance posture | N/A | Drive roadmap sizing and security testing follow-up |
| Marketing/Product Teams (readers) | Consume reports and one-pagers | Power BI; shared PPT/Commons links | Stakeholders for insights |

# # 6. Functional Requirements

1. FR-1 (Authentication): The system shall authenticate internal users via McCain AAD and vendors via separate email-based credentials provisioned by the platform team.
2. FR-2 (Role-based access): The system shall enforce role-based access so that each role views/edits only the information permitted (e.g., vendors: proposal/SIF submission and file uploads; SL: own tests; admins: all tests).
3. FR-3 (RFP creation): The system shall allow Sensory UX Leads to create an RFP, select vendors, and generate a unique ProposalID (format YYS####) that is added to the Project Tracker.
4. FR-4 (RFP distribution): Upon RFP submission, the system shall generate a shareable link and notify selected vendors via email (Power Automate).
5. FR-5 (Vendor proposal submission): Vendors shall be able to submit proposal documents with name and cost estimate (with selected currency) through the Vendor Portal.
6. FR-6 (1-Pager & approvals): The system shall allow SLs to assemble a 1-Pager and route for LM and SD approvals with comment and return-for-change capabilities.
7. FR-7 (Final signoff): The system shall record SL final signoff of the approved proposal and notify the vendor.
8. FR-8 (Test creation IDs): The system shall create a TestID upon approval (format typically YY[A/S]#### as per workflow; Analytical noted as YYA####) and link all subsequent artifacts to that TestID.
9. FR-9 (SIF orchestration): The system shall generate and route the Sample Information Form (SIF) for completion by the R&D Lead, enable SL review/approval, and then provide the vendor view to complete codes/equipment/packaging.
10. FR-10 (Micro Clearance): The system shall auto-create a Micro Clearance Form and route it to the R&D Lead for acknowledgement; upon acknowledgement, update status to "Micro Cleared" and notify SL and vendor.
11. FR-11 (Vendor files): The system shall enable vendors to upload raw data (CSV) and sensory report files to designated sections; all files shall be stored in the Enterprise Data Platform/SharePoint test folder.
12. FR-12 (Analytical workflow): The system shall allow Analytical Leads to create analytical tests, assign R&D Leads to complete SIF fields, upload raw analytical data with basic validation, and complete the test without approvals.
13. FR-13 (Data transformation engine): The system shall transform vendor raw data into a normalized structure via an intermediate file process that displays mapping scores and allows DA to annotate "remove", "mismatch" (with corrected question ID), or "new" (with details).
14. FR-14 (Output ingestion): The system shall generate an output file from the intermediate file and ingest normalized data into the sensory schema tables used by Power BI after test completion.
15. FR-15 (Reporting): The system shall expose Power BI dashboards to visualize tests, products, and results, with filters such as region and test type.
16. FR-16 (Notifications): The system shall notify relevant roles on key events (vendor submissions, approvals, status changes, PO reminder) via email.
17. FR-17 (Admin: vendors): Data Admins shall be able to add/manage vendors in the app and trigger license/access requests to the platform team.
18. FR-18 (Admin: dropdowns): Data Admins shall be able to manage dropdowns, including dependent lists (e.g., country → region) and three-level hierarchies.
19. FR-19 (Admin: bypass): Data Admins shall be able to bypass approval steps when approvers are unavailable, with audit capture.
20. FR-20 (Admin: reference lists): Data Admins shall be able to manage reference lists used by the transformation engine (e.g., attributes, questions) through the app or bulk processes.
21. FR-21 (UX: search/filter): The system shall provide improved search and filter capabilities for completed tests (by region, test type, product, etc.).
22. FR-22 (UX: export SIF): The system shall allow exporting the Sample Information Form to Excel and/or PDF.
23. FR-23 (UX: bulk SIF input): The system shall allow bulk copy/paste (multi-row) into SIF fields to reduce manual entry.
24. FR-24 (UX: one-pager download): The system shall allow downloading a standardized one-pager populated from entered fields for sharing with stakeholders.
25. FR-25 (UX: PPT generation): The system shall generate a PowerPoint deck pre-populated with key fields for the McCain Sensory Report template.
26. FR-26 (Data quality on input): The system shall validate and standardize inputs (e.g., normalize blanks/NA, prevent duplicate entries in controlled vocabularies) prior to saving to SQL.
27. FR-27 (Completion gate): The system shall prevent test completion until Data Admin confirms data transformation is complete (with an explicit confirmation step and/or rule).
28. FR-28 (Post-completion edits): Data Admins shall be able to edit key data elements (including raw data corrections and SIF fields) after test completion and have changes propagate to the sensory schema and reports with audit logs.
29. FR-29 (Multi-collaboration): The system shall allow multiple assigned users (e.g., multiple SLs) to edit an active test concurrently or with controlled handoff without reassignment friction.
30. FR-30 (Non-product tests): The system shall allow creation and completion of tests that do not require an SIF (e.g., research-only), without breaking the workflow.
31. FR-31 (Study mapping): The system shall auto-suggest Study Name(s) based on entered Project Number and allow admin approval for creating new Study entries, eliminating the current email/Excel workflow.
32. FR-32 (Dropdown scoping): The system shall scope dropdown lists to the correct category context (e.g., primary package type shows only primary options; exclude delivery/secondary types).

# # 7. Non-Functional Requirements (NFRs)

# Performance

1. NFR-1: The system shall support global usage for approximately 50–100 users within the first year without degradation in core workflows.
2. NFR-2: The system shall perform basic data validations and transformation processing in a timely manner suitable for routine test cycles (no specific SLA stated).

# Security & Access

1. NFR-3: Internal user authentication shall leverage McCain AAD; external vendors shall use separate email-based credentials controlled by R&D/platform team.
2. NFR-4: Role-based access controls shall restrict vendors to their submissions and limit internal users to their tests and peers’ completed tests; admins can access all.
3. NFR-5: External access and data exchange with vendors shall be secured to protect sensitive product/test information (mechanisms to be confirmed).

# Availability & Reliability

1. NFR-6: The system shall support business-hours availability globally; incident response is currently reactive via vendor support resources.
2. NFR-7: Key workflow statuses and approvals shall be reliably stored and retrievable for concluded and active tests.

# Usability & UX

1. NFR-8: Forms shall minimize horizontal scrolling and optimize layout for laptop usage.
2. NFR-9: Uploaded files/links shall be clearly visible without requiring users to click each link to verify presence.
3. NFR-10: The system shall offer improved search, filter, and export capabilities for SIF and completed tests.
4. NFR-11: The system shall support bulk inputs for SIF and multi-user collaboration on active tests.

# Auditability & Logging

1. NFR-12: Approvals (LM/SD), bypass events, and post-completion edits shall be logged and auditable.
2. NFR-13: Transformation mapping decisions (remove/mismatch/new with IDs) shall be captured and traceable to the test.

# Compliance & Privacy

1. NFR-14: Micro Clearance acknowledgements shall be recorded to support food safety compliance for non-production samples.

# Data Quality

1. NFR-15: Input standardization shall normalize blanks/NA and prevent duplicate dictionary entries (e.g., attributes, packaging types).
2. NFR-16: Transformation matching thresholds shall be configurable, and system behavior shall preserve admin corrections; learning across runs must be clarified.

# # 8. Data Requirements

# ## 8.1 Entities / Objects

- Proposal (ProposalID YYS####), Test (TestID, e.g., YYA####/sensory), Project Tracker
- One-Pager, Approvals (LM/SD), Final Signoff
- Sample Information Form (SIF): product info, cooking instructions, holding protocol, equipment, packaging
- Micro Clearance Form (acknowledgement date)
- Vendor Proposal (doc, cost estimate, currency)
- Screener, Questionnaire (if applicable)
- Raw Data (vendor CSV), Intermediate File (mapping), Output File (normalized)
- McCain Sensory Report (PPT), Simplified report (Commons link)
- Reference Lists: Questions, Answer Options, Attributes, Category Mapping
- Dropdown Dictionaries: Countries, Regions, Packaging Types (primary/secondary/delivery), Equipment
- Study, Project Number, Budget/PO Reminder (manual fields)
- User/Role, Vendor, Notifications
- Schemas/Tables: Sensory schema (for Power BI), R&D schema (app/dropdowns/notifications/holding tables)

# ## 8.2 Key fields & validations (if stated)

- ProposalID format: YYS#### (generated at RFP creation).
- TestID format: created upon approval (e.g., YYA#### for Analytical; sensory TestID upon approval).
- Project Number: used to suggest/populate Study Name; new Study requires admin approval.
- Lot Codes: vendor verification captured in SIF vendor view.
- Sample Codes: vendor numeric/name codes to ensure matching to raw data.
- Dropdown validations: category-scoped packaging types; dependent country/region lists.
- Data transformation: question ID mapping, score thresholds, comments (remove/mismatch/new) with corrected question ID or new question details.
- Budget/PO fields: PO number, dates, costs (tracking only; no external integration).

# ## 8.3 Data quality rules (if stated)

- Normalize blanks/NA values and prevent duplicate entries in dictionaries (e.g., packaging types, attributes).
- Enforce category-filtered dropdowns to reduce misclassification (e.g., primary vs delivery bag types).
- Maintain audit trail of mapping decisions and post-completion edits with propagation to reporting tables.
- Hold data in app (R&D schema) until test completion; push to sensory schema only after completion and validation.

# # 9. Integrations & Interfaces

- Systems involved:
  - Power Apps (Stakeholder & Vendor Portals), Power Automate (emails/links/PO reminders), SQL DB (sensory & R&D schemas), Power BI (reporting), Enterprise Data Platform/SharePoint (file storage), McCain AAD (internal auth).
- Direction & triggers:
  - Inbound: Vendor submissions (proposals, SIF codes/equipment/packaging, raw data CSVs, reports).
  - Transformation: Intermediate file review produces Output file for ingestion to sensory schema on completion.
  - Outbound: Notifications to users/vendors via email; Power BI reads from sensory schema.
- Frequency/events:
  - Event-driven (RFP submission, approvals, SIF/Micro clearance, vendor uploads, transformation completion, test completion).
- Error handling expectations (if stated):
  - Incidents handled by vendor support (Power Apps/Python) reactively; recurring issues were observed post go-live and have stabilized.
- Future integrations (out of scope now): SAP/Coupa for PO/vendor master; TraceGains for supplier/ingredient data.

# # 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Power BI dashboards for tests/products/results; counts/completions by region, test type; selection of products to display.
- Filters/dimensions:
  - Region, test type, product, and other relevant attributes as captured.
- Intended users:
  - Internal stakeholders (Sensory UX, R&D, LM/SD, Marketing/Product).

# # 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - No formal SLAs stated; transformation and validations expected to complete within routine test timelines.
- Operational ownership/support model (if stated):
  - Two vendor resources (Power Apps and Python) handle incidents; enhancements are Phase 2. User/vendor provisioning via platform team (Kaushal).
- Observability:
  - No proactive monitoring tools described; issues raised by users via online form and tracked in Excel; need confirmation of availability/performance/security monitoring.

# # 12. Risks, Dependencies, and Assumptions

- Risks:
  - UX limitations in Power Apps increase time-on-task and user frustration.
  - Transformation matching quality low in worst cases; no realized learning across runs increases manual burden.
  - External vendor access implies security risk; security testing status unclear.
  - Manual admin tasks (study mapping, dropdown management) done via SQL/Excel can introduce errors.
- Dependencies:
  - BlackStraw support team for incidents and future enhancements.
  - McCain AAD and platform team for access/license provisioning.
  - Power Automate for notifications; SharePoint/EDP for file storage; Power BI for reporting.
  - Vendor cooperation on templates and timely data submissions.
- Assumptions:
  - Global user base remains approximately 50–100 within first year; forms primarily used on laptops.
  - Analytical workflow remains approval-light with only basic validation needs.

# # 13. Timeline & Milestones

| Milestone | Date/Period | Notes |
| --- | --- | --- |
| Requirements Finalization (Phase 1) | Oct 2024 | SOW/requirements finalized; development commenced |
| Initial Completion Claimed | Early Feb 2025 | App not ready; continued intensive fixes through Feb |
| Go-Live | Early Mar 2025 | App in production; stabilized basic functions within ~3 months |
| Support Model | Post-Mar 2025 | Incident-only support by vendor (Power Apps & Python) |
| Phase 2 Sizing Request | By early Jun 2025 | IT to provide ballpark estimate and schedule |
| Phase 2 Delivery (estimate) | 3–6 months (TBD) | Dependent on resourcing; parallel workstreams possible |

# # 14. Open Questions (to finalize BRD)

- What specific security testing (penetration, vulnerability scans) has been completed for the external Vendor Portal? If none, what is the plan and timeline?
- Are there defined performance targets (e.g., page load, upload/transform times) and concurrency expectations for 50–100 global users?
- Can the transformation engine be enhanced to retain learning from admin corrections across tests? What is the target matching quality and how will it be measured?
- What audit requirements apply to DA post-completion edits and approval bypass? What fields should be editable and how will propagation be controlled?
- What gating rule should block test completion (e.g., explicit DA confirmation flag) and how to handle exceptions?
- What fields and layout are required for the downloadable one-pager and PPT generation templates? Who will own the templates?
- For multi-collaboration, should the system support true concurrent editing or controlled check-out/check-in with merge rules?
- For non-product tests, what minimal metadata is required when SIF is not applicable?
- Confirm EDP repository details (SharePoint structure, retention), and any required metadata for file storage and retrieval in reports.
- Clarify the "IMS"/vendor master integration intent and systems involved; confirm if SAP/Coupa integration is planned for Phase 3.
- What monitoring/observability tools (availability/performance) should be applied for proactive detection and alerting?
- Confirm user growth expectations beyond year one and any regional data residency or privacy considerations.

# # 15. Source Notes

- Primary notes used: INPUTS_TEXT (RnD Sensory - Roadmap Discussion transcript, May 30, 2025).
- Brownfield notes used: Final Sensory Workflow - Flow Diagram.pdf.