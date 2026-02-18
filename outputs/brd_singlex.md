# Business Requirements Document (BRD) — R&D Sensory UX Data Platform Phase 2 Enhancements

# # 0. Header Information

- Project Name: R&D Sensory UX Data Platform – Phase 2 Enhancements
- Date: 2025-05-30
- Status: Draft
- Document Owner: R&D Sensory UX (Angela Li) and Data Admin (Jenn Soong)
- Version: 0.1

# # 1. Executive Summary

- Purpose: Enhance the existing R&D Sensory UX application to drive data-led product and consumer insights with greater efficiency, accuracy, and usability.
- What is being built: Phase 2 improvements to workflows (pre-approval, multi-user edits), vendor portal, data transformation engine oversight, admin data editing, UX, search/filtering, and data quality controls.
- Who benefits: Sensory UX leads, line managers, sensory directors, R&D leads, analytical team members, and external accredited sensory agencies (vendors).
- Intended outcomes: Faster project setup and approvals, reduced manual effort in data transformation, higher data quality, better visibility of uploads/status, and structured data foundation for predictive analytics.
- Context: System went live in early March 2025 with a stakeholder portal, vendor portal, and data transformation engine; initial stabilization completed with ~45 incidents tracked and resolved/improving.
- Future vision: Connect broader product/process/material data, improve question/attribute matching, and enable predictive analytics (longer-term, not Phase 2).

# # 2. Business Context & Problem Statement

- Background / context:
  - Previously no systematic tool for R&D Sensory User Experience data; historical data was transactional and trend analysis took days to months.
  - Custom application delivered with three components: Stakeholder portal (internal), Vendor portal (external agencies), and a Data Transformation Engine.
  - Data stack includes Power Apps front-end, SQL database (R&D and Sensory schemas), and Power BI reports; ~35 tables in total (19 initially, expanded for app).
- Current state (if stated):
  - Go-live: Early March 2025 (effective March 1). ~3 months in production at meeting time.
  - Incidents: ~45 logged; stabilization improving; support by Blackstraw team (1 Power Apps dev, 1 Python engineer).
  - Global usage across Europe, APAC, and North America; expected 50–100 users within a year (varies by projects).
- Problem / pain points:
  - UX issues: Excessive scrolling; poor layout; poor visibility of uploaded file status; admin list management clunky; difficult to manage 700 questions/500 attributes via UI.
  - Workflow gaps: No pre-approval stage before sending RFP to vendors; only one assignee can edit active tests; cannot capture non-product tests (SIF is mandatory); line managers cannot complete full workflow.
  - Data transformation: Question/attribute matching accuracy lower than expected in cases (~65% worst cases); no observed improvement over time; high manual validation workload.
  - Data admin: No ability to edit data after test completion and propagate to reporting tables; bulk copy/paste into SIF not supported; no SIF export.
  - Data quality: Duplicate/variant values due to blanks/NA and inconsistent dropdowns (e.g., primary package type list includes non-primary items).
  - Monitoring/security: Reactive incident handling; security/performance testing and observability not confirmed.
- Why now / business drivers:
  - Reduce manual effort and cycle time across proposal, testing, transformation, and reporting.
  - Improve data quality and structure to enable historical trend insights and set foundation for predictive analytics.
  - Address stakeholder experience issues and remove workarounds (e-mail approvals, manual SQL edits, Excel trackers).
  - Align with fiscal planning and feature prioritization for Phase 2 budget sizing.

# # 3. Objectives & Success Metrics

- Objectives:
  - Introduce a pre-approval step before RFP issuance and allow manager/director edits prior to vendor engagement.
  - Enable data admin edits after test completion with propagation to reporting (sensory schema) tables.
  - Reduce manual effort in data transformation by improving matching workflows and reusing mappings.
  - Improve UX: minimize scrolling, better file status visibility, bulk SIF operations, refined dropdowns, enhanced search/filter.
  - Support non-product tests without requiring SIF; allow multi-user collaboration in active tests.
- Success metrics / KPIs (where stated or implied):
  - Stabilization baseline: ~45 incidents logged to date; aim to reduce new incidents post-Phase 2 (target to be defined).
  - Matching quality: Observed worst-case ~65% match accuracy; target improvement approach to be defined (e.g., decreased manual corrections).
  - User adoption/capacity: Support expected 50–100 global users in year one.
- Baseline (if stated):
  - Go-live early March 2025; ~3 months in production; ~45 incidents tracked; matching reported as low as ~65% in some cases.
- Measurement cadence & owners (if stated):
  - Incident tracking via Excel by Angela Li / Jenn Soong; Power BI usage inferred via completed/active tests; formal cadence to be defined.

# # 4. Scope

| In Scope (Phase 2) | Out of Scope (Phase 2) |
| --- | --- |
| Pre-approval workflow prior to RFP issuance; allow manager/director edits and vendor change notifications | Building a new predictive analytics application (long-term objective only) |
| Data admin edits after test completion with propagation to reporting tables | Replacing Power Apps platform or complete UI re-platforming |
| Enhanced data transformation oversight (mapping reuse, flags, manual overrides) | Fully automated ML-based self-learning with guaranteed accuracy improvements (to be defined later) |
| Support non-product tests (no SIF required) with appropriate workflow | End-to-end integration with SAP/Coupa vendor master and PO systems (proposed for later phase) |
| Multi-user collaboration on active tests (multiple editors) | Rewriting historical data outside defined transformation workflows |
| Bulk copy/paste into SIF; SIF export (Excel/PDF) | Expanding to new data domains beyond sensory/analytical without defined requirements |
| Improved UX: file status visibility, minimized scrolling, refined dropdowns, improved search/filter | Major UI redesign beyond achievable Power Apps capabilities (unless feasible within constraints) |
| Gate test conclusion until data transformation is completed by DA | Non-approved tooling for external data capture beyond vendor portal architecture |
| Data quality checks to standardize entries and prevent duplicates | Automated user behavior analytics not requested |
| Extend role capabilities (line managers to complete full workflow); admin dropdown management | Automated licensing workflows (manual contact with Kaushal remains) |
| Auto-populate study name from project number with approval path for new studies | Global content localization/internationalization beyond current needs |

- Constraints (only what is stated):
  - Power Apps UI limitations cited by vendor; complexity and time constraints impacted UX enhancements in Phase 1.
  - Vendor portal users require licenses; internal users added via Active Directory but still need platform team provisioning.
  - Reactive monitoring; security/performance testing status unknown.
  - Data from external vendors varies; partial standardization via templates; transformation must accommodate variability.
  - Support resources limited to incident resolution, not feature enhancements (per vendor agreement).

# # 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Create RFPs, manage test workflow, coordinate with vendors, submit reports; initiate/complete tests | Own tests and peers’ completed tests; dashboard; file uploads; can sign off; receives notifications | Primary user; will gain pre-approval flow and gating checks |
| Line Manager | Approve one-pager/proposals; review reports; may oversee testing | Approval screens; comments; can send back for changes | Phase 2: allow completing full workflow where applicable |
| Sensory Director | Approve proposals and final reports; provide comments/requests for changes | Approval screens; comments | Pre-approval capability needed before RFP issuance |
| R&D Lead | Provide sample information (SIF), cooking instructions, holding/delivery protocols; micro clearance date | SIF entry pages; micro clearance entry | May collaborate with Sensory Lead; bulk SIF ops desired |
| Analytical Lead | Internal analytical tests (instrument measurements); upload raw data and reports (no approvals) | Analytical workflow screens; data uploads | Simpler workflow vs sensory |
| Vendor (External) | Submit proposals; enter sample codes; upload test results/reports; provide equipment info | Vendor portal with limited view; only their proposals/test submissions; notifications on submission | Authenticated via separate email-based accounts; licensed |
| Data Admin (Angela Li / Jenn Soong) | Administer data, manage dropdowns, oversee transformation, validate mappings, coordinate incidents | Admin view with all tests; manage vendors/users/dropdowns; bypass approvals | Phase 2: post-completion data edits; admin dropdown tables; study master automation |
| Power Apps Developer (Blackstraw) | Support incidents related to app workflows/UI | Admin access (vendor side) | Named as Azhar/Azure (clarify); support only incidents |
| Python Engineer (Blackstraw) | Support transformation engine and data processing incidents | Back-end access | Named as Rahul; supports data transformation |
| Platform/Licensing (Kaushal) | Provision licenses and access for users, including vendors | N/A | Manual provisioning on request |
| Customer Relationship Manager (Blackstraw) | Engagement oversight and escalation | N/A | Named as Subhanil |

# # 6. Functional Requirements

1. FR-1 (Pre-approval): The system shall provide a pre-approval step for one-pager details before any RFP is sent to vendors, enabling line managers and sensory directors to review and request changes.
2. FR-2 (Manager/Director Edits): The system shall allow line managers and sensory directors to request and/or make edits to pre-RFP fields (e.g., background, objectives) and upon approval, mark the one-pager as approved for RFP.
3. FR-3 (Vendor Change Notification): When pre-RFP details are updated after initial vendor visibility, the system shall notify affected vendors and require re-submission of proposals as applicable.
4. FR-4 (Post-Completion Edits): The system shall allow Data Admins to edit data (including SIF and raw data) after a test is marked completed and propagate those changes to the reporting (sensory schema) tables.
5. FR-5 (Audit Post-Completion): The system shall record an audit trail of post-completion edits capturing editor, timestamp, fields changed, and reason.
6. FR-6 (Non-product Tests): The system shall support creating and completing sensory/analytical projects that do not require a Sample Information Form (SIF), with an alternate workflow that does not break.
7. FR-7 (Multi-user Editing): The system shall allow multiple authorized users (e.g., multiple sensory leads and/or R&D leads) to contribute to an active test concurrently or sequentially without requiring reassignment.
8. FR-8 (Bulk SIF Entry): Users shall be able to bulk copy/paste tabular data into SIF sections (e.g., product details, cook instructions, holding/delivery protocols).
9. FR-9 (SIF Export): Users shall be able to export the SIF (per test) to Excel and/or PDF.
10. FR-10 (File Status Visibility): The system shall display clear visual indicators of which files have been uploaded in each section (vendor files, reports, etc.) without requiring users to click each link.
11. FR-11 (Improved Search/Filter): Users shall be able to filter and search completed tests by attributes such as region, test type (consumer, descriptive, analytical), product/SKU, vendor, and status.
12. FR-12 (Dropdown Conditioning): The system shall constrain dropdown lists (e.g., primary package type vs secondary/delivery types) to only show values relevant to the field’s category.
13. FR-13 (Study Auto-population): The system shall auto-suggest study names based on the entered project number and allow selection from existing valid mappings.
14. FR-14 (New Study Request): If a project number has no mapped study name, the system shall allow submitting a new study request to Data Admins for approval and creation.
15. FR-15 (Admin Dropdown Tables): Admins shall be able to manage dropdown lists (including hold protocol values and multi-level country/region hierarchies) via an app table interface rather than requiring direct SQL edits.
16. FR-16 (Gate Test Conclusion): When a sensory lead attempts to conclude a test, the system shall verify that the data transformation step is completed by Data Admins; if incomplete, it shall block conclusion and prompt the user.
17. FR-17 (Notifications): The system shall send e-mail notifications to relevant roles at key workflow steps (e.g., vendor submission; approvals requested; SIF ready; transformation actions required; test concluded).
18. FR-18 (Vendor Portal Access): External vendors shall authenticate using separate email-based accounts and shall only view/submit data pertinent to their assigned proposals/tests.
19. FR-19 (Approvals): The system shall support approvals for one-pagers and final reports by line managers and sensory directors with ability to approve or request changes and capture comments.
20. FR-20 (Bypass Approval – Admin Only): Admins shall retain the ability to bypass an approval stage when approvers are unavailable, logging the action with justification.
21. FR-21 (Transformation – Mapping Review): The system shall present question/attribute mapping scores and flags (exact, check, poor) for Data Admin review and allow marking items as keep, remove, mismatch (with corrected question ID), or new (with details).
22. FR-22 (Transformation – Mapping Reuse): The system shall store and reuse Data Admin mapping decisions (e.g., corrected question IDs) to reduce repeated manual work across studies.
23. FR-23 (Transformation – Re-upload): The system shall permit re-uploading vendor raw data and intermediate files if issues are found and regenerate output aligned to database structure.
24. FR-24 (Reporting): The system shall provide Power BI datasets/report feeds reflecting completed and approved tests, including product lists, results, counts by region/test type, and product selection filters.
25. FR-25 (Role Enhancement – Line Manager): The system shall enable line managers who oversee testing to complete the full sensory workflow where applicable, not only the RFP portion.
26. FR-26 (RFP Vendor Selection): The system shall support soliciting proposals from one or multiple vendors and allow the sensory lead to select the preferred vendor.
27. FR-27 (Budget/PO Tracking): The system shall capture budget/PO tracking fields (e.g., PO number, cost, dates) for team tracking (no external system integration in Phase 2).

# # 7. Non-Functional Requirements (NFRs)

- Performance:
  - NFR-1: The system should support expected usage of 50–100 global users in the first year without material degradation of responsiveness.
  - NFR-2: Performance test approach and acceptable response thresholds shall be defined and executed prior to Phase 2 release (see Open Questions).
- Security & Access:
  - NFR-3: External vendors shall authenticate with separate email-based credentials; internal users shall authenticate via Active Directory.
  - NFR-4: Role-based access control shall restrict users to their own tests and completed peer tests as currently applied; vendors shall only access their submissions.
  - NFR-5: Security testing (including for external vendor access) shall be conducted prior to Phase 2 go-live; findings shall be remediated.
- Availability & Reliability:
  - NFR-6: Implement basic availability monitoring and alerting for the application (URL health checks) with notifications to support.
  - NFR-7: Incident management shall continue with defined ownership by vendor support; SLAs to be confirmed (see Open Questions).
- Usability & UX:
  - NFR-8: Minimize horizontal/vertical scrolling through improved layout and grouping; provide clear visual status for uploads.
  - NFR-9: Admin list management shall be table-based and scalable for large question/attribute sets (hundreds of entries).
- Auditability & Logging:
  - NFR-10: Approval actions and comments shall be logged with timestamps and users.
  - NFR-11: Post-completion data edits by admins shall be fully audit-logged (who, when, what changed).
- Compliance & Privacy:
  - NFR-12: External access shall comply with organizational security policies for third-party access; data shared shall be limited to study context.
- Data Quality:
  - NFR-13: Enforce standardization of blank/NA values and prevent creation of duplicate/variant entries via validation rules.
  - NFR-14: Dropdown conditioning shall prevent misclassification by restricting category values to relevant options.

# # 8. Data Requirements

- 8.1 Entities / Objects:
  - Proposal (RFP) and One-pager
  - Test (Sensory: consumer/descriptive; Analytical)
  - Sample Information Form (SIF): Product info, cooking instructions, holding/delivery protocol
  - Vendor, Equipment, Vendor Files
  - Micro Clearance (date)
  - Budget/PO tracking (PO number, cost, dates)
  - Project Number and Study Name (mapping)
  - Raw Data, Intermediate File, Output File
  - Questions, Attributes, Code Legend (for mapping questions/answers)
  - Dropdown Lists (country/region hierarchies; packaging types; protocols)
  - Notifications and Workflow Statuses
- 8.2 Key fields & validations (if stated):
  - Product: SKU, lot code, category (e.g., fry product, appetizer).
  - SIF: Detailed cooking instructions; holding/packaging/delivery protocol types and parameters.
  - Vendor: Proposal details, cost estimates; sample codes per product that match raw data.
  - Micro clearance: Date field (for pilot line samples).
  - Project/Study: Project number must map to a valid study name or trigger a new study request.
  - Validations: Dropdown conditioning for package types; standardize blanks/NA; prevent duplicate value creation.
- 8.3 Data quality rules (if stated):
  - Standardize representations of missing values; normalize synonymous entries.
  - Restrict categories to appropriate options (e.g., primary package type should not show secondary/delivery items).
  - Reuse corrected question mappings to reduce repeated manual intervention.
  - Prevent completion of tests until transformation is validated and output generated.

# # 9. Integrations & Interfaces

- Systems involved:
  - Power Apps application (stakeholder and vendor portals)
  - SQL database with R&D and Sensory schemas (~35 tables total)
  - Data Transformation Engine (intermediate and output files)
  - Power BI (reporting)
  - Email notifications
  - Active Directory (internal users); separate email-based auth (vendors)
- Direction & triggers:
  - Inbound: Vendor submissions (proposals, codes, raw data, reports) via vendor portal.
  - Internal: One-pager approvals; SIF entry; micro clearance; admin mapping; test conclusion.
  - Transformation: Vendor raw → intermediate (mapping/validation) → output structured for DB ingestion.
  - Outbound: Completed/approved data to Power BI datasets/reports.
- Events/frequency:
  - Event-driven per workflow stage (submission, approval, upload, conclusion).
- Error handling expectations (if stated):
  - Flag poor/ambiguous mappings for admin review; allow re-upload of raw/intermediate files; block test conclusion if transformation incomplete.
- Future/Phase 3 (not Phase 2):
  - Potential integration with SAP/Coupa for vendor master/PO (timing TBD).

# # 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Power BI reports showing products tested, test results, counts by region/test type, and product selection filters.
- Filters/dimensions:
  - Product/SKU, region, test type (consumer, descriptive, analytical), vendor, status.
- Intended users:
  - Internal stakeholders (sensory leads, line managers, sensory directors, R&D leads, analytical leads).

# # 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - Not formally stated; support is incident-focused by vendor (Power Apps dev and Python engineer).
- Operational ownership/support model (if stated):
  - Blackstraw support: Power Apps developer (Azhar/Azure), Python engineer (Rahul); Customer relationship manager (Subhanil).
  - Licensing/access provisioning by Kaushal (platform team).
  - Reactive incident intake via online form and Excel tracker; observability currently not implemented.

# # 12. Risks, Dependencies, and Assumptions

- Risks:
  - Lower-than-expected question/attribute matching accuracy increases manual workload and time-to-insight.
  - UX limitations may continue to hinder user efficiency if not adequately addressed within platform constraints.
  - Security/performance testing gaps introduce risk given external vendor access.
  - Blocking test conclusion may delay timelines if transformation backlogs occur.
- Dependencies:
  - Vendor (Blackstraw) support for incident resolution and any agreed enhancements.
  - Platform team (Kaushal) for license/access provisioning.
  - External vendors’ data submission formats and timeliness.
  - Future SAP/Coupa integration decisions for vendor master/PO linkage (out of Phase 2).
- Assumptions:
  - Internal AD remains the mechanism for internal users; external vendors continue with separate email-based authentication.
  - Power Apps remains the delivery platform for Phase 2.

# # 13. Timeline & Milestones

- Key milestones/dates (if stated):
  - Initial solution design/requirements: Oct 2024 (finalized late Sep/early Oct).
  - Go-live: Early March 2025 (effective March 1).
  - Production stabilization: ~3 months post go-live; ~45 incidents tracked.
  - Phase 2 estimation: Requested by week following the 2025-05-30 meeting.
- Release approach (if stated):
  - Discussion indicated Phase 2 delivery potentially within 3–6 months depending on resourcing and parallelization (to be confirmed).

# # 14. Open Questions (to finalize BRD)

1. OQ-1: What are the performance targets (e.g., page load/response times) and the performance testing plan/tools for Phase 2?
2. OQ-2: What is the scope and timing of security testing for external vendor access, and who owns remediation?
3. OQ-3: Should post-completion data admin edits require any approval, or is audit logging sufficient?
4. OQ-4: What exact conditions constitute “data transformation complete” for gating test conclusion (e.g., output generated, mapping flags cleared)?
5. OQ-5: Confirm the user concurrency assumptions and regional usage patterns to size performance testing.
6. OQ-6: For transformation mapping improvements, should the system implement mapping reuse only, or also target an accuracy improvement metric?
7. OQ-7: Which fields must appear in the downloadable one-pager PPT and report templates (finalized format)?
8. OQ-8: Confirm the process for non-product tests (required fields, approval steps) and whether both sensory and analytical workflows will support it.
9. OQ-9: Clarify support SLAs (response/resolution times) and support hours for Power Apps and transformation incidents.
10. OQ-10: Confirm the name/contact of the Power Apps support developer (Azhar/Azure) and any backup resources.
11. OQ-11: Define timeline and scope for potential SAP/Coupa integration (vendor master/PO) beyond Phase 2.
12. OQ-12: Confirm if any additional UX constraints exist within Power Apps that could impact specific Phase 2 UX changes.

# # 15. Source Notes

- Primary notes used: INPUTS_TEXT (RnD Sensory - Roadmap Discussion-20250530_173643 Meeting transcript)
- Brownfield notes used: Not provided