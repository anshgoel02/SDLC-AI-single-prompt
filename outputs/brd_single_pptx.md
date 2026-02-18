# Business Requirements Document: R&D Sensory UX Data Platform — Phase 2 Enhancements

# 0. Header Information

- Project Name: R&D Sensory UX Data Platform (Stakeholder & Vendor Portals + Data Transformation) — Phase 2 Enhancements
- Date: 2025-05-30 (based on roadmap discussion meeting)
- Status: Draft

# 1. Executive Summary

- Purpose: Enhance the existing Sensory UX data platform to improve workflow efficiency, data quality, and usability for R&D sensory, analytical, and vendor stakeholders.
- What is being built: Phase 2 improvements to the Stakeholder Portal, Vendor Portal, and Data Transformation Module; key features include pre-RFP approvals, post-completion data edits, improved matching engine supervision, multi-collaborator support, UX upgrades, and data quality controls.
- Who benefits: Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Analytical Leads, Vendors, and Data Admins (global users across EU/APAC/NA).
- Intended outcomes: Faster approvals and vendor coordination, reduced data transformation effort, higher data accuracy, better discoverability of completed tests, and reduced admin burden.
- Reporting: Continued Power BI reporting on standardized sensory schemas with improved filter/search usability needs.
- Future outlook: Lays groundwork for predictive analytics and potential integrations (e.g., SAP/Coupa, ingredient/spec management), while keeping Phase 2 focused on platform usability and data quality.

# 2. Business Context & Problem Statement

- Background / context:
  - Existing platform (live since early March 2025) supports sensory and analytical workflows via Stakeholder and Vendor Portals and a Data Transformation Module feeding a SQL database and Power BI.
  - Data originates mostly from external accredited sensory agencies (consumer and descriptive analysis), plus internal analytical (instrument) tests.
- Current state (if stated):
  - Application launched March 2025; stabilized after initial hypercare; ~45 incidents logged; now basic functions stable.
  - Internal users via AD (manual access enablement by platform team); external vendors use separate email-based accounts (license needed per vendor).
  - Power BI reports run primarily on sensory schema tables; app uses R&D schema as holding tables until test completion.
- Problem / pain points:
  - UX is cumbersome (excessive scrolling, left-right layouts, poor link visibility, limited filters/search).
  - Data Transformation matching quality is inconsistent; supervised learning promised but not improving across runs; heavy manual review of intermediate files.
  - No post-completion data edit capability through the app; corrections require direct DB intervention.
  - Workflow gaps: No pre-RFP alignment step; non-product research tests cannot skip Sample Information Form; only one active editor per test; conclusion can occur before data transformation completes.
  - Admin burdens: Managing large drop-down lists and hold/packaging protocols via SQL; limited admin UI; vendor/user provisioning overhead.
- Why now / business drivers:
  - Enable efficient, accurate insights from sensory data without prolonged manual effort.
  - Support global usage growth (expected 50–100 users within a year) and scale vendor collaborations.
  - Prepare structured, high-quality data foundations for future predictive analytics and potential ERP/vendor integrations.

# 3. Objectives & Success Metrics

- Objectives:
  - Introduce pre-RFP approvals and role-appropriate editing to prevent rework with vendors.
  - Enable post-completion edits (with audit) that propagate to sensory schema and reports.
  - Reduce manual workload in data transformation by improving supervised matching review and controls.
  - Improve UX discoverability and efficiency (filters, link visibility, layout, bulk entry/export).
  - Extend workflow flexibility (non-product tests, multi-collaboration, line manager end-to-end capability).
  - Strengthen data quality controls prior to SQL persistence.
- Success metrics / KPIs (no explicit numbers stated):
  - Reduction in manual review time per test in transformation step.
  - Reduction in UX-related support tickets/incidents post-release.
  - Increase in proportion of tests concluded with verified transformed data.
- Baseline (if stated): Not quantified in notes.
- Measurement cadence & owners (if stated): Not specified; Data Admins currently track incidents in Excel.

# 4. Scope

## 4.1 In Scope

- Stakeholder & Vendor Portals and Data Transformation Module Phase 2 enhancements:
  - Pre-RFP approval workflow and editing (manager/director) before vendor notification.
  - Propagation of approved pre-RFP changes to vendors, including re-submission when needed.
  - Admin/super-admin post-completion data edits that update sensory schema and reports.
  - Data transformation supervision improvements (matching review UI/controls, persistence of overrides).
  - Gate test conclusion until data transformation is verified complete by Data Admins (or provide strong inline reminder as interim).
  - Support for non-product research tests (skip Sample Information Form).
  - Allow multiple collaborators to work on active tests; extend line manager role to complete full workflow where applicable.
  - UX improvements: layout/scrolling; show clearly which files are uploaded; enhanced search/filters for completed tests; bulk copy/paste into SIF; SIF export to Excel/PDF; contextual dropdown filtering.
  - Admin management UI for hold/packaging protocols and large controlled lists (reduce need for SQL).
  - Auto-populate study name by project number; workflow to request/approve new study entries; notifications.
  - Data quality checks prior to SQL persistence (e.g., blanks/NA normalization, duplicate detection).
  - Notifications for key workflow events (existing pattern via email to continue).
  - Maintain current reporting (Power BI) on sensory schema with improved discoverability needs captured.

## 4.2 Out of Scope

- Predictive analytics/modeling and formulation prediction (future ambition).
- Integration with SAP/Coupa (vendor master, PO data) in this phase.
- Ingredient/spec/COA/allergen master data management by third-party tools (e.g., TraceGains).
- Changes to licensing/provisioning processes managed by platform team (external vendor licensing).

## 4.3 Constraints (only what is stated)

- Platform UX limitations observed in current Power Apps implementation.
- External vendors require separate accounts and licenses; provisioning involves platform team (Kaushal).
- Vendor data formats vary; full standardization at source is not feasible.
- Support resources (1 Power Apps developer, 1 Python engineer) currently limited to incident resolution.
- Budgeting timelines near fiscal year end; estimate requested within a week of 2025-05-30 meeting.

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Owns RFP creation, coordinates vendor submissions, completes test data and report submission, initiates/acknowledges test conclusion. | Access to own tests; can see peers’ completed tests. | Primary workflow owner. |
| Line Manager | Approves one-pager/proposals; in Phase 2, complete end-to-end workflow where they oversee tests. | Approval views; dashboard. | Needs extended capability to complete tests. |
| Sensory Director | Final approvals on proposals and reports; provides comments/returns for changes. | Approval views; dashboard. | Approval authority. |
| R&D Lead | Provides Sample Information Form (product details, cooking/holding protocols); micro clearance date. | Inputs SIF; views assigned tasks. | Feeds vendor with preparation details. |
| Analytical Lead | Submits internal analytical test info and data (no approvals). | Analytical workflow screens. | Simpler workflow than sensory. |
| Vendor (External) | Submits proposals, codes samples, uploads raw data/reports, acknowledges instructions. | Vendor Portal with limited info; separate email-based login. | License required per vendor; notifications to Sensory Lead. |
| Data Admin (e.g., Angela Li, Jenn Soong) | Administer data, supervise transformation (intermediate/output files), manage drop-downs, bypass approvals, user/vendor management requests. | Admin view (all tests, admin menus); Power BI; SQL access. | Wants post-completion edit capability via app; aims to reduce SQL reliance. |
| Platform/Access Team (e.g., Kaushal) | Provision user access/licenses (internal AD and external vendors). | N/A | Provisioning outside the app; emails required. |

# 6. Functional Requirements

1. FR-1: The system shall provide a pre-RFP approval step in which Line Managers and Sensory Directors can review and approve the one-pager before any RFP is sent to vendors.
2. FR-2: The system shall allow Line Managers and Sensory Directors to edit designated pre-RFP fields (e.g., background, objectives, product details) prior to vendor notification.
3. FR-3: The system shall propagate approved pre-RFP changes to impacted vendor RFPs and notify vendors to revise proposals as required.
4. FR-4: The system shall enable Data Admins to edit test data after test completion, with all edits persisted to the sensory schema and reflected in reports.
5. FR-5: The system shall record an audit trail of all post-completion edits, including user, timestamp, field changed, and before/after values.
6. FR-6: The system shall prevent test conclusion unless Data Admins verify that data transformation for the test is complete; a configurable override may be provided to Admins.
7. FR-7: The system shall continue to display match confidence scores for transformed questions/attributes and allow Admin overrides (remove/mismatch with corrected ID/new).
8. FR-8: The system shall persist Admin overrides from transformation reviews and reuse them to improve subsequent matching behavior for identical cases.
9. FR-9: The system shall support tests that do not require Sample Information Forms (non-product research), allowing creation and completion of such projects without SIF.
10. FR-10: The system shall allow multiple authorized users to concurrently contribute to an active test’s data entry (e.g., Sensory Leads, delegates), with field-level locking or conflict resolution as needed.
11. FR-11: The system shall allow Line Managers to complete the full sensory test workflow when they oversee a test (not limited to the RFP stage).
12. FR-12: The system shall provide bulk copy/paste (and/or bulk upload) capabilities for entering Sample Information Form data.
13. FR-13: The system shall provide export of Sample Information Form data to Excel and/or PDF.
14. FR-14: The system shall display clear visual indicators of whether expected files are uploaded in each section (vendor files, reports) without requiring users to click each link.
15. FR-15: The system shall provide improved search and filter capabilities for completed tests (e.g., by region, test type, products, status).
16. FR-16: The system shall constrain dropdown lists to contextually relevant values (e.g., primary package type lists only primary options, excluding secondary/delivery types).
17. FR-17: The system shall provide admin UI to manage controlled lists (e.g., hold/packaging protocols, equipment) to reduce the need for direct SQL updates.
18. FR-18: The system shall auto-populate available study names when a known project number is entered; if no study exists, users can request creation of a new study entry.
19. FR-19: The system shall notify Data Admins when a new study is requested and allow approval to add it to the study master without leaving the app.
20. FR-20: The system shall support generation of a one-pager output (PowerPoint) populated from entered fields for sharing with stakeholders.
21. FR-21: The system shall support generation of the McCain report template (PowerPoint) populated from entered fields.
22. FR-22: The system shall maintain existing email notifications for key events (e.g., vendor submission, approvals, assignments) and extend to new gating/approval steps as required.
23. FR-23: The system shall continue to use internal AD for internal users and separate email-based authentication for vendors.
24. FR-24: The system shall not require budget system integration; budget/PO fields remain for team tracking only.
25. FR-25: The system shall ensure that any edits to raw/transformed data are re-ingested to maintain alignment between app views and the reporting schema.

# 7. Non-Functional Requirements (NFRs)

## Performance

1. NFR-1: The system shall undergo performance testing to assess response times and behavior under expected usage (global users; growth to 50–100 users over a year).
2. NFR-2: The system shall support bulk data entry/export operations in the Sample Information Form without timeouts under typical dataset sizes encountered.

## Security & Access

1. NFR-3: The system shall undergo security testing appropriate for external vendor access, including authentication and authorization validation.
2. NFR-4: The system shall enforce role-based access so that vendors view/submit only their assigned data and internal stakeholders see only permitted tests.
3. NFR-5: Provisioning for external vendors shall remain controlled through the platform team process; the app shall not bypass existing licensing controls.

## Availability & Reliability

1. NFR-6: The system shall implement basic observability/availability monitoring with alerts to support teams for outages or degraded performance.
2. NFR-7: The system shall provide stable workflows that prevent data loss or inconsistent states during approvals, gating, and post-completion edits.

## Usability & UX

1. NFR-8: The system shall minimize horizontal scrolling and provide intuitive, readable layouts for complex forms.
2. NFR-9: The system shall clearly indicate file upload status and provide improved filtering/search for completed tests.
3. NFR-10: The system shall support collaboration without users blocking each other unnecessarily.

## Auditability & Logging

1. NFR-11: The system shall log key workflow events (approvals, submissions, conclusion) and post-completion edits for audit purposes.
2. NFR-12: The system shall log transformation override actions (remove/mismatch/new) with user and timestamp.

## Compliance & Privacy

1. NFR-13: The system shall ensure external vendor access does not expose internal data beyond the minimum necessary for test execution.

## Data Quality

1. NFR-14: The system shall perform pre-save validations to standardize blanks/NA and prevent common duplication in controlled lists.
2. NFR-15: The system shall ensure final transformed data conforms to the target sensory schema structure for reporting.

# 8. Data Requirements

## 8.1 Entities / Objects

- Proposal / RFP (one-pager; vendor proposals; approvals).
- Test (sensory/analytical) with statuses and dashboards.
- Sample Information Form (product info, cooking instructions, holding/packaging protocols).
- Micro Clearance (date).
- Vendor (account, equipment used).
- Equipment (per vendor; extendable).
- Project/Study (project number to study names).
- Raw Data (vendor submissions).
- Intermediate File (reformatted with match mapping, code legend, override comments).
- Output File (normalized stacked structure for DB ingestion).
- Product details (SKU, log code).
- Questions/Attributes and Answer Options (reference library).

## 8.2 Key fields & validations (if stated)

- Product SKU and log code (required for sample mapping; vendor codes must map via code legend).
- Micro clearance date required for non-production pilot samples.
- Dropdowns must be contextually filtered (e.g., primary vs secondary vs delivery packaging types).
- Project number to study name mapping (auto-populate if exists; request workflow if new).
- Transformation match score visibility and override fields: remove, mismatch with corrected question ID, new with metadata.

## 8.3 Data quality rules (if stated)

- Normalize blanks/NA values consistently before saving to SQL.
- Prevent duplicate entries in controlled lists (e.g., hold/packaging protocols).
- Only ingest completed and verified transformed data into sensory schema.
- Maintain audit trail for all overrides and post-completion edits.

# 9. Integrations & Interfaces

- Systems involved:
  - Stakeholder Portal (Power Apps) — internal users via AD.
  - Vendor Portal (Power Apps) — external vendors with separate email-based accounts.
  - Data Transformation Module — transforms raw vendor data to target schema (Python-supported).
  - SQL Database — R&D schema (holding/app), Sensory schema (reporting).
  - Power BI — reports on sensory schema.
- Direction / flow:
  - Vendor uploads → Transformation (intermediate/output) → Sensory schema → Power BI (outbound to reporting).
- Triggers/events/frequency:
  - Event-driven on vendor submissions, approvals, Admin verifications; no fixed batch schedule stated.
- Error handling expectations:
  - Transformation step must surface match scores and allow Admin overrides; ingestion occurs only after verified output.
  - No integration to budget/PO systems in this phase; fields remain manual.

# 10. Reporting / Analytics

- Dashboards/reports required:
  - Power BI dashboards showing products tested, results, counts by region, test type, completion status.
- Filters/dimensions:
  - Region, test type (sensory/analytical; consumer/descriptive), products, status; enhanced search/filters for completed tests requested.
- Intended users:
  - Internal stakeholders and Data Admins; peers can view completed tests.

# 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated): Not specified.
- Operational ownership/support model:
  - Post-hypercare support by vendor team: 1 Power Apps developer and 1 Python engineer focused on incident resolution; enhancements are not in current support scope.
  - User/vendor provisioning requires platform team involvement (Kaushal).
  - Incident tracking currently maintained by Data Admins (Excel).

# 12. Risks, Dependencies, and Assumptions

- Risks:
  - Continued UX constraints in platform could limit improvements.
  - Transformation matching quality may remain suboptimal without effective learning persistence.
  - Security/availability gaps if testing and monitoring are not implemented.
  - High admin burden if post-completion edits and admin list management remain via SQL.
- Dependencies:
  - Platform/access team for user/vendor provisioning and licenses.
  - Vendor IT support (Power Apps, Python) for implementation of enhancements.
  - External vendors for timely and correct data submissions (formats vary).

# 13. Timeline & Milestones

- Key milestones/dates (if stated):
  - Phase 1: Requirements finalized Oct 2024; go-live early March 2025.
  - Phase 2: Ballpark estimate requested by early June 2025; expected delivery window discussed as 3–6 months (dependent on resourcing).
- Release approach (if stated): Not specified.

# 14. Open Questions (to finalize BRD)

1. What specific fields are editable in the pre-RFP stage by Line Managers and Directors, and which should remain read-only?
2. Should pre-RFP edits trigger mandatory vendor re-submission or allow minor changes without re-submission? Define rules.
3. What audit retention period is required for post-completion edits and transformation overrides?
4. What are the target performance thresholds (e.g., response times) and peak concurrent usage expectations?
5. What is the required scope and tooling for security testing and ongoing availability monitoring?
6. What collaboration model is preferred for multi-editor scenarios (e.g., field locking, check-in/out, or last-write-wins)?
7. What is the desired threshold/logic for reusing transformation overrides (scope across studies/vendors/categories)?
8. What is the acceptance criterion for improved matching (e.g., baseline match quality targets) and how will improvements be measured?
9. What export formats are mandatory for Sample Information Form (Excel, PDF, both) and any standardized templates?
10. Who approves new study creation requests and what fields are required for the study master?
11. Are there file size/type limits for vendor uploads that need to be enforced or updated?
12. Any regional data privacy considerations for global users and external vendors that impact access/logging?

# 15. Source Notes

- Primary notes used: INPUTS_TEXT (RnD Sensory - Roadmap Discussion meeting transcript, 2025-05-30).