# R&D Sensory UX Data Platform - Phase 2 BRD

# # 0. Header Information

- Project Name: R&D Sensory UX Data Platform (Stakeholder & Vendor Portals + Transformation Engine)
- Date: 2026-02-19
- Status: Draft
- Document Owner: R&D Sensory UX (Angela Li, Jenn Soong)
- Version: 0.1

# # 1. Executive Summary

- Purpose: Enhance the existing R&D Sensory UX data application to improve data quality, usability, and workflow efficiency across sensory and analytical testing.
- What is being built: Phase 2 enhancements to the Power Apps solution comprising the Stakeholder Portal, Vendor Portal, and Data Transformation Module, plus reporting improvements.
- Who benefits: Sensory UX leads, R&D leads, line managers, sensory directors, analytical leads, and approved external vendor partners.
- Intended outcomes: Faster, more accurate ingestion of sensory/analytical data; reduced manual effort; improved approvals and governance; better visibility and search in completed tests; foundations for future predictive analytics.
- Key themes: Pre-approval workflow, multi-user collaboration, bulk data handling, enhanced file visibility, data transformation accuracy, data quality standardization, UI/UX improvements, and gating to protect data integrity.
- Out of scope: Predictive analytics, deep product information integration, and enterprise system integrations (e.g., SAP/Coupa) in this phase.

# # 2. Business Context & Problem Statement

- Background / context:
  - A Power Apps-based solution went live in early March 2025 to capture sensory (consumer and descriptive) and analytical data via a Stakeholder Portal, Vendor Portal, and a Data Transformation engine. Data resides in Azure SQL (sensory schema) and feeds Power BI.
  - The app supports global users (Europe, APAC, North America) with vendor submissions and internal approvals, and centralizes sample preparation details (SIF), micro clearance, and reports.
- Current state (if stated):
  - In production ~3 months as of May 30, 2025; ~45 incidents tracked initially (stabilizing). Hypercare ended; two vendor resources provide incident-only support (Power Apps dev and Python engineer).
  - Stakeholder Portal shows active and completed tests; Vendor Portal supports proposals, sample code entry, and test file uploads. Power BI reports visualize tests by region, test type, product, etc.
- Problem / pain points:
  - Poor UX (excessive scrolling, left-right navigation, limited file/link visibility, clunky admin lists).
  - Data Transformation engine match accuracy is below expectations (observed ~65% in worst cases vs. claimed 95%); supervised learning not improving over time.
  - No pre-approval step prior to RFP causes churn; inability for DA to edit completed tests and propagate to reporting tables; non-product research projects cannot bypass SIF.
  - Single-user lock on active tasks; lack of bulk copy/paste and export for SIF; limited search/filter on completed tests.
  - Data quality issues (e.g., blanks/NA, duplicates) and non-scoped dropdowns leading to errors.
- Why now / business drivers:
  - Enable data-driven product and consumer insights with efficiency and accuracy; reduce manual rework and cycle time; improve data integrity and auditability; prepare structured data for future predictive analytics and potential integrations.

# # 3. Objectives & Success Metrics

- Objectives:
  - Introduce pre-approval and gating to ensure accurate RFPs and protect data integrity through to ingestion.
  - Improve UX to reduce user effort (bulk operations, visibility, search/filter) and support multi-user collaboration.
  - Increase accuracy and efficiency of the Data Transformation engine and intermediate file review.
  - Enhance data quality controls and dropdown scoping to reduce duplicates and errors.
  - Support non-product research projects without requiring SIF.
- Success metrics / KPIs (use exact numbers if present):
  - Target user base capacity: support 50–100 users within the first year globally.
  - Reduce manual intermediate file review time per study (baseline not stated; measure delta after release).
  - Decrease incident rate from initial ~45 hypercare issues to a stable, low volume (track post-release trend).
  - Increase match verification acceptance rate on first pass (track % of questions with acceptable matches without manual correction).
- Baseline (if stated):
  - No quantified baseline for transformation accuracy other than observations (worst case ~65% match).
- Measurement cadence & owners (if stated):
  - Not stated; Data Admins (Angela Li, Jenn Soong) currently monitor via incidents and manual tracking.

# # 4. Scope

## ## 4.1 In Scope

- Stakeholder Portal enhancements: pre-approval before RFP; editable RFP with propagation and re-approval; multi-user collaboration; gating test conclusion on Data Transformation completion; improved search/filter for completed tests; one-pager export.
- Vendor Portal enhancements: clearer file visibility; dropdown category scoping; maintain equipment list; notifications.
- Data Transformation Module improvements: configurable match thresholds, verification workflow with comments, improved mapping UX, and accurate ingestion to sensory schema.
- Data quality controls: standardize NA/blank handling, deduplication checks, dropdown scoping (e.g., holding protocol types).
- SIF efficiency: bulk copy/paste, export (Excel/PDF), and support for projects without SIF (non-product research).
- Admin functions: dropdown management, bypass approvals, category mapping, hold protocol management, automatic study name from project number with approval, post-completion edit capability for Data Admins with propagation to reporting tables.
- Reporting: improve filters/search on completed tests; Power BI consumption of final sensory schema remains.
- Security & access: maintain role-based access, external vendor authentication via email-based accounts, internal users via AD.

## ## 4.2 Out of Scope

- Building predictive analytics or formulation success prediction.
- Full integration with supplier/spec systems (e.g., TraceGains) in this phase.
- Integration with SAP/Coupa (vendor master, PO) in this phase.
- Mobile/tablet form factor optimization (laptop-only continues).
- Redesign of Power BI content beyond adding filters/search in the app context.

## ## 4.3 Constraints (only what is stated)

- Power Apps UX limitations cited by current vendor; previous pushback on more advanced UI layouts.
- External vendors require separate licensed access; provisioning coordinated with platform team.
- Support team is incident-only; enhancements require separate budgeting and planning.
- Laptop form factor only due to data entry volume.
- Global user base across regions (Europe, APAC, North America).

# # 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Initiate RFP; manage test workflow; send one-pager for approval; coordinate vendor; upload McCain report; conclude test | Own tests; peers' completed tests | Primary workflow owner for sensory studies |
| Line Manager | Approve RFP/one-pager; review final report; may oversee testing | Approval views | Needs capability to complete workflow if overseeing testing |
| Sensory Director | Approve RFP/one-pager and reports; provide comments | Approval views | Final approver |
| R&D Lead | Provide Sample Information Form (SIF) details; micro clearance date | SIF entry for assigned tests | Receives notifications to complete SIF |
| Analytical Lead | Initiate and manage analytical tests (simplified workflow, no approvals); upload data/reports | Analytical workflow screens | Internal instrument measures (e.g., texture, oil) |
| Vendor | Submit proposals; enter sample codes; indicate equipment used; upload test files/reports | Limited to their proposals, SIF codes, uploads | External users; separate email-based login |
| Data Admin | Oversee data quality; manage dropdowns; category mapping; bypass approvals; user mgmt; verify transformation; manage intermediate/output files; admin all tests | Admin view (all tests, admin menus) | Can add vendors/internal users (with platform support); requires post-completion edit capability |
| Platform/IT (AD/Access) | Provision access/licenses for users (internal and external) | N/A | External vendor licenses incur cost; internal users no cost |
| Power Apps Support (Vendor) | Incident resolution for app workflow | N/A | One resource (Power Apps) for incidents only |
| Python/Transformation Support (Vendor) | Incident resolution for transformation engine | N/A | One resource (Python) for incidents only |

# # 6. Functional Requirements

## Stakeholder Portal – Sensory Workflow

1. FR-1: The system shall provide a pre-approval step for the one-pager before any RFP is sent to vendors, requiring Line Manager and Sensory Director approval.
2. FR-2: The system shall allow authorized users (Sensory UX Lead) to edit RFP/one-pager fields prior to vendor submission and, if edited after vendor submission, shall propagate changes to impacted vendors and trigger re-approval.
3. FR-3: The system shall route one-pager approvals to Line Manager and Sensory Director with approve/reject and comment capture; rejections shall return the item to the Sensory UX Lead for revision.
4. FR-4: The system shall support multi-user collaboration on active tests, allowing more than one Sensory UX team member to edit the same test workflow stages as configured by the owner.
5. FR-5: The system shall capture SIF (product info, cooking instructions, holding protocol, delivery simulation, equipment) and allow bulk copy/paste of SIF entries from spreadsheets.
6. FR-6: The system shall support projects without SIF (non-product research) by allowing test creation and progression without SIF dependencies.
7. FR-7: The system shall capture micro clearance date from the R&D Lead and display clearance status to the Vendor.
8. FR-8: The system shall allow the Sensory UX Lead to upload the final McCain report and route it for Line Manager and Sensory Director approval with comments.
9. FR-9: The system shall gate test conclusion: concluding a test shall be blocked until Data Admins confirm Data Transformation completion for the study.
10. FR-10: The system shall provide a Completed Tests view where users can view finalized test artifacts and entries.
11. FR-11: The system shall provide improved search and filter for completed tests (e.g., by region, country, test type, product, status).
12. FR-12: The system shall allow authorized Data Admins to edit test data even after test completion, and such edits shall propagate to the sensory schema tables and downstream reporting.
13. FR-13: The system shall generate a one-pager PowerPoint from entered fields and allow download of the one-pager for sharing.
14. FR-14: The system shall allow export of SIF data to Excel and/or PDF.
15. FR-15: The system shall automatically suggest Study Name(s) based on entered Project Number; if a new Study Name is proposed, it shall route to Data Admin for approval and creation in Study Master.

## Vendor Portal

1. FR-16: The system shall allow vendors to view RFP details and submit proposals and cost estimates.
2. FR-17: The system shall allow vendors to view SIF (as read-only) and enter sample codes that map to their raw data.
3. FR-18: The system shall allow vendors to indicate equipment used, selecting from a vendor-specific list or adding new entries.
4. FR-19: The system shall allow vendors to upload files to designated sections (e.g., raw data, reports), with clear on-screen indicators of uploaded vs. missing files.
5. FR-20: The system shall restrict vendors to only their own proposals, samples, and file uploads.
6. FR-21: The system shall notify the Sensory UX Lead via email upon vendor submissions (proposals, files).

## Data Transformation Module

1. FR-22: The system shall allow upload of raw data received from vendors in varying formats.
2. FR-23: The system shall generate an Intermediate File that maps submitted questions to database questions with match scores and flags based on configurable thresholds (e.g., exact, check, poor).
3. FR-24: The system shall allow Data Admins to annotate the Intermediate File with standardized comments (blank=accept, remove, mismatch+[corrected question ID], new+[new question details]).
4. FR-25: The system shall generate the Output File, restructuring responses to the database format (e.g., stacked per respondent/product) and assigning question IDs based on verified mappings.
5. FR-26: The system shall ingest the Output File into the sensory schema tables only upon completion of mapping verification.
6. FR-27: The system shall display and store match scores for each question and provide a dashboard or view to prioritize poor or ambiguous matches for review.
7. FR-28: The system shall maintain a code legend linking sample codes to products for accurate mapping.

## Admin & Configuration

1. FR-29: The system shall allow Data Admins to manage dropdown lists and dependent lists (e.g., country, region) within the app.
2. FR-30: The system shall allow Data Admins to manage category mapping used by the transformation engine.
3. FR-31: The system shall scope dropdowns by category (e.g., primary package type only shows primary options; secondary/delivery types not shown).
4. FR-32: The system shall provide a bypass approvals feature for admins to advance items when approvers are unavailable, with audit logs.
5. FR-33: The system shall allow Data Admins to manage Hold Protocol entries and streamline duplicate terms.
6. FR-34: The system shall allow Admins to add vendors and internal users within the app and trigger provisioning requests to the platform team for account/license setup.

## Security & Access

1. FR-35: The system shall authenticate external vendors via separate email-based user accounts (not internal AD).
2. FR-36: The system shall authenticate internal stakeholders via Active Directory.
3. FR-37: The system shall enforce role-based access so that: internal users see their tests and peers' completed tests; vendors see only their items; admins see all.

## Notifications

1. FR-38: The system shall send email notifications to Sensory UX Leads upon vendor submissions (proposals, files).
2. FR-39: The system shall send email notifications to R&D Leads when SIF input is requested.
3. FR-40: The system shall notify approvers (Line Manager, Sensory Director) when items require approval and upon resubmission.
4. FR-41: The system shall notify Data Admins when a new Study Name is proposed or when transformation verification is pending.
5. FR-42: The system shall display an on-screen reminder when a Sensory UX Lead attempts to conclude a test before Data Transformation is marked complete.

# # 7. Non-Functional Requirements (NFRs)

## Performance

1. NFR-1: The system shall support at least 100 named users globally in the first year.
2. NFR-2: The system shall handle concurrent vendor uploads and internal edits without data loss (response time targets to be defined).

## Security & Access

1. NFR-3: External vendor access shall be isolated from internal AD; accounts are provisioned per vendor email and licensed accordingly.
2. NFR-4: Role-based access controls shall be enforced throughout the application and data layers.
3. NFR-5: Security testing for the externally accessible vendor portal shall be conducted and documented (scope and tooling TBD).

## Availability & Reliability

1. NFR-6: The system shall provide basic availability monitoring and alerting for outages (e.g., URL probes) with notifications to support.
2. NFR-7: The system shall provide error handling for failed uploads/transformation steps with clear messages and retry capability.

## Usability & UX

1. NFR-8: High-usage forms (e.g., SIF, approvals) shall minimize scrolling and lateral navigation and present clear sectioning.
2. NFR-9: File/link visibility shall clearly indicate uploaded vs. missing items without requiring individual link clicks.
3. NFR-10: Bulk operations (copy/paste SIF entries, exports) shall be supported to reduce manual data entry.
4. NFR-11: Laptop form factor shall be supported as the primary interface.

## Auditability & Logging

1. NFR-12: All approvals, rejections, comments, and bypass actions shall be logged with user, timestamp, and context.
2. NFR-13: Post-completion edits by Data Admins shall be audited with before/after values and user attribution.

## Data Quality

1. NFR-14: The system shall standardize common nulls (e.g., blanks, NA) and prevent duplicate master entries through validation.
2. NFR-15: Dropdowns shall be category-scoped to prevent invalid selections (e.g., primary vs. secondary package types).

# # 8. Data Requirements

## ## 8.1 Entities / Objects (if stated)

- Proposal/RFP (one-pager, background, objectives, actions, approvals)
- Test (Sensory; Analytical)
- Sample Information Form (SIF): product info (SKU, lot code, category), cooking instructions, holding protocol, delivery simulation, equipment
- Micro Clearance (date, status)
- Vendor (accounts, equipment list)
- User/Roles (internal AD users, external vendor users)
- Approvals (LM/Director approvals, bypass)
- Files/Reports (vendor raw data, vendor reports, McCain report)
- Raw Data / Intermediate File / Output File (question mappings, scores, comments)
- Questions/Attributes (reference lists for consumer/descriptive tests)
- Category Mapping (product categories to attribute sets)
- Hold Protocol / Packaging Types
- Project Number / Study Master (mapping)
- Budget/PO Tracking (PO number, raised/received, cost)

## ## 8.2 Key fields & validations (if stated)

- Project Number: drives Study Name suggestions; new entries require admin approval.
- Study Name: unique within Project Number context where applicable.
- Product: SKU, lot code, category; sample codes (vendor-provided) must map to products in code legend.
- Micro Clearance: date required for non-production samples prior to testing.
- PO Tracking: PO number, raised/received dates, cost (for internal tracking only).
- Transformation: question ID, match score, comment (remove/mismatch/new) must be validated before ingestion.
- Dropdown scoping: primary/secondary/delivery types separated and validated per field.
- Standardization: normalize blanks/NA; prevent duplicate master entries (e.g., hold protocol terms).

## ## 8.3 Data quality rules (if stated)

- Match scores must be recorded for all mapped questions and flagged when below configurable thresholds for review.
- Intermediate File comments must be one of: blank (accept), remove, mismatch+[correct ID], new+[details].
- SIF entries must not be saved with invalid dropdown selections (scoped lists only).
- New Study Names require admin review to avoid duplicates.

# # 9. Integrations & Interfaces

- Systems involved:
  - Power Apps application (Stakeholder & Vendor Portals).
  - Azure SQL Database (sensory schema; ~35 tables total across app and sensory schemas; 19 initial sensor schema tables).
  - Power BI reports (consuming sensory schema tables).
  - Active Directory for internal users; external email-based accounts for vendors.
  - Email notifications for workflow events.
- Direction / data flow:
  - Vendor uploads → Data Transformation (raw → intermediate → output) → sensory schema tables → Power BI.
  - Stakeholder inputs (RFP, SIF, approvals) → app tables → (on completion) persisted to sensory schema.
- Triggers/events/frequency:
  - Notifications on vendor submissions, approval requests, SIF requests, transformation pending/completed, and test conclusion attempts.
- Error handling expectations:
  - Clear error messages on failed uploads/transformation; ability to re-upload raw/intermediate files; do not ingest to final tables until verification complete.
- Future (out of scope this phase):
  - Potential integration with SAP/Coupa for vendor master/PO; supplier/spec platforms (e.g., TraceGains).

# # 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Power BI reports showing products tested, results, count of tests by region and test types.
- Filters/dimensions:
  - Region, country, test type (consumer/descriptive/analytical), product, status.
- Intended users:
  - Internal stakeholders (Sensory UX Leads, R&D Leads, Line Managers, Sensory Directors, Data Admins).

# # 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - None stated for response times or availability; performance/security testing status unclear.
- Operational ownership/support model (if stated):
  - Incident-only support by vendor: one Power Apps developer and one Python (transformation) engineer; issues tracked in internal tooling and Excel; reactive monitoring.
- User provisioning via platform/IT; external vendor licenses required.

# # 12. Risks, Dependencies, and Assumptions

- Risks:
  - UX limitations may hinder adoption and efficiency.
  - Low transformation match accuracy increases manual workload and risk of errors.
  - No confirmed security/performance testing for external vendor portal exposure.
  - Lack of availability monitoring leads to reactive issue discovery.
  - Post-completion edit capability without proper audit could impact data integrity if not well controlled.
- Dependencies:
  - Platform/IT for user provisioning and external license management.
  - Vendor support (Power Apps, Python) for incident resolution and potential enhancements.
  - Power BI for reporting consumption; Azure SQL sensory schema for final data.
  - External vendors for timely proposal/data submissions.

# # 13. Timeline & Milestones

- Key milestones/dates (if stated):
  - Requirements finalized: October 2024 (Phase 1).
  - Go-live: Early March 2025; ~3 months in production as of May 30, 2025.
- Release approach (if stated):
  - Phase 2 window discussed as 3–6 months (to be refined based on detailed sizing).

# # 14. Open Questions (to finalize BRD)

1. OQ-1: What are the target response times and concurrency expectations for key workflows (e.g., SIF save, file upload)?
2. OQ-2: What security testing (if any) has been completed for the external vendor portal, and what additional testing is required (scope, tools, timing)?
3. OQ-3: What availability monitoring and alerting approach should be implemented (tooling, alert recipients, thresholds)?
4. OQ-4: What is the acceptable transformation match accuracy threshold for auto-accept vs. review (define score bands)?
5. OQ-5: Who approves post-completion edits by Data Admins, and what audit/reporting is required for such edits?
6. OQ-6: Define the exact one-pager PPT template fields and layout for automated export.
7. OQ-7: Confirm the full list of dropdowns requiring scoping (e.g., primary vs. secondary package types) and authoritative value lists.
8. OQ-8: For non-product research projects, what minimum fields are required to create and complete a test without SIF?
9. OQ-9: Should Line Managers have full Sensory Lead capabilities when overseeing testing, or a subset? Specify permissions.
10. OQ-10: What filters/search criteria are required for Completed Tests (final list) and should these be mirrored in Power BI?
11. OQ-11: Confirm expected user growth beyond 100 users and any regional constraints that impact access or data residency.
12. OQ-12: Are there near-term integration priorities (e.g., SAP/Coupa for PO fields) that must be designed for, even if not delivered in Phase 2?

# # 15. Source Notes

- Primary notes used: INPUTS_TEXT (RnD Sensory - Roadmap Discussion-20250530 meeting transcript).
- Brownfield notes used: None provided.