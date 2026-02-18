# BRD – R&D Sensory UX Data Platform (Phase 2 Enhancements)

# # 0. Header Information

| Field | Value |
| --- | --- |
| Project Name | R&D Sensory UX Data Platform – Phase 2 Enhancements |
| Date | 2026-02-18 |
| Status | Draft |
| Document Owner | Angela Li (R&D Sensory UX); Jenn Soong (Data Admin) |
| Version | 0.1 |

# # 1. Executive Summary

- Purpose: Enhance the existing R&D Sensory UX data application to improve data quality, usability, vendor collaboration, and analytical readiness.
- What is being built: Phase 2 feature set focused on pre-RFP approvals, post-completion data editability, improved AI-driven data transformation, UX upgrades, and workflow flexibility (e.g., non-product tests, multi-user editing).
- Who benefits: Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Data Admins, and external Vendors across global regions.
- Intended outcomes: Faster and more accurate ingestion of vendor data, reduced manual remediation, better governance of approvals and conclusion, improved reporting readiness for Power BI.
- Context: Current app is live (since early March 2025), globally used, with ~50–100 expected users in year one; UX pain points and transformation matching accuracy are key improvement areas.
- Longer-term vision: Prepare foundation for predictive analytics by strengthening structured sensory and analytical data capture and quality.

# # 2. Business Context & Problem Statement

- Background/context:
  - Custom Power Apps solution with Stakeholder Portal, Vendor Portal, and Data Transformation Engine supports Sensory UX (consumer, DA-Spectrum) and Analytical (instrument) workflows.
  - Data flows include RFP → Vendor proposal → Approvals → SIF (Sample Information Form) → Micro Clearance → Vendor raw data/report → Data transformation → Reporting (Power BI).
- Current state:
  - App went live ~March 1, 2025; ~35 SQL tables (19 initial sensory schema + additional R&D/app tables); global users; internal auth via AAD; vendors via separate email-based credentials.
  - Power BI dashboards consume sensory schema; PO/budget tracked in-app but not integrated with SAP/Coupa; support is reactive (2 Blackstraw resources: Power Apps and Python).
- Problem/pain points:
  - UX is cumbersome (excessive scrolling, poor file visibility, limited search/filter, contextual dropdown issues, no bulk SIF paste/export).
  - Data Transformation Engine (question/attribute matching) accuracy below expectations; lacks learning/improvement despite supervised feedback.
  - Governance gaps: No pre-RFP approval step; inability for Data Admins to edit data post test completion; risk of concluding tests before data transformation finishes.
  - Operational: Vendor license management overhead; manual dropdown maintenance; reactive incident management; ~45 issues logged in early months.
- Why now/business drivers:
  - Reduce time to analyze historical sensory data (currently can take days to months) and increase accuracy and efficiency of insights to support product development.
  - Prepare data foundations for predictive analytics and innovation while improving global user adoption and experience.

# # 3. Objectives & Success Metrics

- Objectives:
  - Introduce governance for pre-RFP approvals and prevent premature test conclusion before data transformation sign-off.
  - Enable post-completion data edits by Data Admins with traceability.
  - Improve data transformation mapping accuracy and reduce manual reconciliation.
  - Elevate UX to support efficiency (bulk SIF actions, contextual dropdowns, export, search/filter, clear file status).
  - Support additional use cases (non-product tests) and multi-user collaboration on active tests.
- Success metrics / KPIs (targets to be confirmed):
  - Reduced manual transformation review effort per test (baseline not provided).
  - Improved mapping acceptance rate prior to manual intervention (baseline not provided).
  - Decreased incident volume related to UX/data quality (baseline: ~45 early issues).
  - Faster retrieval of historical data for reporting (baseline: days to months).
- Baseline:
  - Not quantified in notes (incidents ~45 in early months; mapping accuracy reported variable 65–95%).
- Measurement cadence & owners:
  - Not stated; to be defined by R&D Sensory UX and Data Admin teams.

# # 4. Scope

## ## 4.1 In Scope

| Feature/Capability | Notes |
| --- | --- |
| Pre-RFP approval workflow | Manager/Director approval of 1-pager prior to sending RFP to vendors; support updating RFP fields and re-notifying vendors. |
| Post-completion data edits | Data Admin ability to edit post-completion data with propagation to sensory schema and traceability. |
| Data Transformation Engine improvements | Improve question/attribute mapping accuracy; enable supervised feedback utilization; reduce manual steps (remove/mismatch/new). |
| UX improvements | Minimize scrolling; clear file-upload visibility; improved search/filter; contextual dropdowns; sample info form export; bulk copy/paste for SIF. |
| Non-product testing workflow | Allow projects without SIF to progress without breaking workflow. |
| Multi-user collaboration | Allow multiple users to work on an active test concurrently (beyond single assignee). |
| Conclusion gating | Block concluding a test until Data Admin confirms transformation complete; reminders/notifications included. |
| Data quality controls | Standardize entries (blanks/NA), dedup, validations prior to SQL save (e.g., holding protocol, packaging types). |
| Role capability extension | Allow Line Managers to complete full Sensory workflow where they oversee testing. |
| Admin dropdown management enhancements | Manage holding protocol tables; differentiate dropdown categories (primary/secondary/delivery types). |
| Study name auto-population | Auto-populate study name from project number; if new, route to admin approval and create in Study Master. |
| Reporting readiness enhancements | Ensure edits propagate to Power BI datasets; maintain status visibility in dashboards. |

## ## 4.2 Out of Scope

| Item | Rationale |
| --- | --- |
| SAP/Coupa integration (vendor master, PO sync) | Identified as future (phase 3) due to wider digital transformation dependencies. |
| Predictive analytics/modeling | Long-term ambition; current phase focuses on data capture, quality, and transformation. |
| Mobile/tablet optimization | Current app used on laptops due to data entry volume; no mobile requirement stated. |
| Building a new standalone predictive application | Team preference not to build custom predictive solution at this stage. |

## ## 4.3 Constraints (only what is stated)

- Platform limitations in Power Apps have impacted UX flexibility (layout, file link visibility, table exports).
- External vendors require separate licensing and credentials; onboarding requires coordination with Kaushal’s platform team.
- Support resources (Power Apps and Python from Blackstraw) currently limited to incident resolution, not enhancements.
- Data variability from multiple vendors limits strict standardization; transformation requires adaptable mapping.
- Security and performance testing status unknown.

# # 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Owns test initiation, RFP, 1-pager, vendor coordination, SIF review, McCain report creation, test conclusion. | Dashboard of personal active/completed tests; can initiate tests; sees proposal/test details. | Primary process owner. |
| Line Manager (LM) | Approves 1-pager and Sensory report; can initiate workflows; may oversee testing. | LM dashboard; approval views. | Needs capability to complete full workflow in some cases (phase 2). |
| Sensory Director (SD) | Final approval of 1-pager and Sensory report; comments. | SD dashboard; approval views. | Approvals required before proceeding. |
| R&D Lead | Completes SIF; micro clearance acknowledgement; provides sample prep details. | R&D dashboard with SIF and micro clearance forms linked by TestID. | Feeds vendor with sample details. |
| Data Admin | Manages transformation engine; verifies question mapping; manages dropdowns, reference lists; admin functions. | Admin dashboard; view/edit all active/completed tests; access/download raw data. | Requires post-completion edit rights (phase 2). |
| Analytical Lead | Creates and completes analytical tests; uploads analytical raw data; basic validation (no complex transformation). | Analytical dashboard (simpler workflow). | Internal instrument-based measurements. |
| Vendor | Receives RFP; submits proposal; completes sections of SIF; runs tests; uploads raw data and reports. | Vendor portal with limited view/submit; notified on status updates. | External users; separate login/licensing; minimal visibility beyond assigned items. |
| Platform/Access Admin (Kaushal’s team) | Provision licenses and access for users (internal and vendor). | N/A | Onboarding via email request from R&D team. |

# # 6. Functional Requirements

## Access & Authentication

1. FR-1: The system shall authenticate internal users via McCain AAD.
2. FR-2: The system shall authenticate external vendors via separate email-based credentials managed by the R&D team and platform admin.
3. FR-3: The system shall restrict vendor access to only their proposals, assigned SIF sections, test uploads, and related notifications.

## Sensory UX Workflow & Approvals

1. FR-4: The system shall support a pre-RFP approval step where the Sensory UX Lead submits a 1-pager for Line Manager and Sensory Director approval prior to sending the RFP to vendors.
2. FR-5: The system shall allow editing of RFP-related fields post manager/director feedback and propagate updates to vendors, notifying them to amend proposals as required.
3. FR-6: The system shall generate a unique ProposalID in the format YYS#### upon initial RFP creation.
4. FR-7: Upon approval, the system shall generate a TestID and transition the record to the active test workflow.
5. FR-8: The system shall allow multiple Sensory UX users to concurrently edit active test records where collaboration is required.
6. FR-9: The system shall enable Line Managers to complete full Sensory workflow steps in cases where they oversee the test.
7. FR-10: The system shall prevent test conclusion until a Data Admin has confirmed data transformation is complete; attempts shall trigger a blocking prompt identifying pending steps.

## Sample Information & Non-Product Tests

1. FR-11: The system shall allow projects/tests to proceed without a Sample Information Form (SIF) where the test is non-product (e.g., research), without breaking the workflow.
2. FR-12: The system shall provide bulk copy/paste capabilities for SIF entries from spreadsheets to reduce manual data entry.
3. FR-13: The system shall enable export of SIF data to Excel and/or PDF.
4. FR-14: The system shall constrain dropdown lists contextually (e.g., primary package type only shows primary options; secondary/delivery types not shown).
5. FR-15: The system shall auto-populate study name options based on the entered project number; if none exist, it shall route a request to Data Admin for approval to create a new study in the Study Master.
6. FR-16: The system shall record micro clearance acknowledgement date by R&D Lead and update status to “Micro Cleared,” notifying relevant users.

## Vendor Portal

1. FR-17: The vendor portal shall allow vendors to view RFP details via shareable link and submit proposals with cost estimates.
2. FR-18: The vendor portal shall allow vendors to complete their SIF sections (e.g., sample codes, equipment used) and view McCain-provided product, cooking, holding, and packaging instructions.
3. FR-19: The vendor portal shall support raw data (CSV) and report uploads, with section-based file submission areas.
4. FR-20: The system shall notify Sensory UX Leads when vendors submit proposals, SIF entries, raw data, or reports.

## Data Transformation & Admin

1. FR-21: The system shall provide a Data Admin interface to manage the transformation engine, including review of intermediate files (reformatted mapping pages) and output files.
2. FR-22: The system shall allow Data Admins to annotate transformation matches as remove/mismatch (with corrected ID)/new, and re-upload intermediate files.
3. FR-23: The system shall apply validated mappings to produce output files aligned to the database’s long-form response structure (e.g., stacked per respondent per product).
4. FR-24: The system shall enable Data Admins to edit data after test completion, with changes propagated to sensory schema tables and made available to reporting.
5. FR-25: The system shall provide admin management of dropdown lists and reference tables (e.g., holding protocol), including deduplication and category mapping.
6. FR-26: The system shall standardize common data entries at save time (e.g., normalize blanks/NA) to prevent duplicates and data quality issues.
7. FR-27: The system shall maintain audit logs for post-completion edits and approvals (who, what, when).

## Reporting & Dashboards

1. FR-28: The system shall ensure that completed and edited test data are available to Power BI via the sensory schema tables.
2. FR-29: The system shall provide improved search and filter capabilities for completed tests (e.g., by region, test type, product).
3. FR-30: The system shall allow download of a one-pager (PPT) populated from captured fields for stakeholder sharing.
4. FR-31: The system shall support generating a McCain report template (PPTX) populated from entered fields where feasible within platform constraints.

# # 7. Non-Functional Requirements (NFRs)

## Performance

- NFR-1: The system should support global usage by approximately 50–100 users in the first year without material degradation in responsiveness.
- NFR-2: The transformation and upload processes should complete within reasonable operational windows for standard test sizes (exact targets TBD).

## Security & Access

- NFR-3: Internal authentication via McCain AAD; external vendor access via separate credentials.
- NFR-4: Role-based access control shall enforce least-privilege (e.g., vendors access only their assigned items).
- NFR-5: The system shall undergo security testing appropriate for external-facing vendor access (status currently unknown).

## Availability & Reliability

- NFR-6: Monitoring and alerting should be established for application availability and key endpoints (current approach is reactive).
- NFR-7: Incident management shall continue with documented tracking of issues and resolutions.

## Usability & UX

- NFR-8: Minimize horizontal/vertical scrolling and improve form layouts for typical laptop usage.
- NFR-9: Provide clear file-upload visibility (e.g., presence indicators per section) to avoid users clicking each link to verify.
- NFR-10: Provide contextual dropdowns to reduce user error (e.g., packaging types).
- NFR-11: Provide bulk SIF paste and export capabilities to/from spreadsheets.
- NFR-12: Improve search and filtering for completed tests.

## Auditability & Logging

- NFR-13: Capture audit logs for approvals, bypass actions, transformations, and post-completion data edits (user, action, timestamp).

## Data Quality

- NFR-14: Enforce normalization of blanks/NA and prevent duplicate records in reference tables (e.g., holding protocol, attributes).
- NFR-15: Validate mapping quality prior to committing transformed data to the sensory schema.

# # 8. Data Requirements

## ## 8.1 Entities / Objects

- Proposal (RFP) [ProposalID: YYS####]
- Test [TestID created post-approval; Analytical TestID format: YYA####]
- One-Pager (approval artifact)
- Sample Information Form (SIF): product info, cooking instructions, holding protocol, packaging, equipment, sample codes, lot codes
- Micro Clearance Acknowledgement (date/status)
- Vendor Raw Data (CSV) and Vendor Reports (files)
- Transformation Intermediate File (reformatted mapping, code legend, comments)
- Transformation Output File (structured data for DB ingest)
- Questions/Attributes & Answer Options (reference list, mapping IDs)
- Equipment, Packaging Types (primary/secondary/delivery)
- Study Master and Project Number mapping
- Users, Roles, Approvals, Audit Logs

## ## 8.2 Key fields & validations

- ProposalID, TestID formats as stated; unique and system-generated.
- SIF required fields: product identifiers (SKU/log code if available), cooking instructions, holding protocol, equipment, packaging types, sample codes, lot codes (vendor verification).
- Micro Clearance: date required for pilot-line samples; status updates to “Micro Cleared.”
- Transformation mapping: question IDs must exist or be created as “new” with required metadata; remove/mismatch/new comments mandatory where applicable.
- Dropdowns: contextual validation (e.g., primary package types only in primary field).
- Study name auto-fill based on project number; new study creation requires admin approval.
- Normalization of blanks/NA and prevention of duplicate entries in reference lists.

## ## 8.3 Data quality rules

- All raw data uploads must pass basic formatting checks prior to transformation.
- All mapped questions must either match existing IDs or be flagged with new IDs and definitions.
- Duplicate reference entries (e.g., holding protocol terms, packaging types) must be merged or removed by Admin.
- Post-completion edits must be logged and propagated to reporting datasets.

# # 9. Integrations & Interfaces

- Systems involved:
  - Power Apps (Stakeholder & Vendor Portals), Python-based Data Transformation Engine, SQL Database (sensory and app schemas), Power BI, EDP/SharePoint (file storage), Power Automate (notifications/links/reminders), McCain AAD (internal auth).
- Direction & triggers:
  - Inbound from vendor: proposals, SIF inputs, raw data CSVs, vendor reports.
  - Transformation engine processes intermediate files to output files for DB ingest; admins re-upload corrected mappings as needed.
  - Power Automate sends shareable RFP links, status notifications, and PO reminders.
- Frequency & events:
  - Event-driven on submissions/approvals; dashboard statuses update per workflow stage.
- Error handling expectations:
  - Validation failures return actionable messages; transformation mismatches flagged for admin intervention; audit trail retained.
- Future integration (out of scope phase 2):
  - SAP/Coupa for vendor master/PO sync.

# # 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Power BI views of products tested, results, test counts by region and test type; completed tests repository for cross-team visibility.
- Filters/dimensions:
  - Region, test type (Consumer Quant, DA-Spectrum, QA-QDA, Analytical), product, status.
- Intended users:
  - Sensory UX Leads, Line Managers, Sensory Directors, R&D Leads, Data Admins.

# # 11. SLAs & Operational Expectations

- SLAs or processing expectations:
  - Not stated; current model is reactive incident handling; no formal performance or uptime targets provided.
- Operational ownership/support model:
  - Two Blackstraw support resources: one for Power Apps (application) and one Python engineer (transformation). Support limited to incidents; enhancements handled separately.
- User provisioning requires emailing Kaushal’s platform team; external vendors require licenses.

# # 12. Risks, Dependencies, and Assumptions

- Risks:
  - Low transformation matching accuracy increases manual effort and delays.
  - Poor UX may reduce adoption and increase data entry errors.
  - Security/performance testing status unknown despite external access (vendors).
  - Reliance on incident-only support slows enhancements and defect resolution.
  - Vendor licensing overhead and onboarding delays (coordination needed).
- Dependencies:
  - McCain AAD for internal auth; vendor credential provisioning via platform team.
  - Power Automate for notifications/links; EDP/SharePoint for file storage; Power BI for reporting.
  - Blackstraw support for Power Apps and Python transformation engine.
  - Future SAP/Coupa integration for vendor/PO data (phase 3).

# # 13. Timeline & Milestones

- Key milestones/dates (if stated):
  - Initial app go-live: ~March 1, 2025 (after early February hardening).
  - Phase 2 plan/estimates: to be provided (discussed as ~3–6 months depending on resourcing; final plan not confirmed).
- Release approach:
  - Not stated; likely iterative delivery to address UX, transformation, and workflow gating first.

# # 14. Open Questions (to finalize BRD)

1. What are the target thresholds for transformation matching accuracy and the approach to enable learning from admin feedback?
2. What governance and audit requirements apply to post-completion data edits (e.g., approver needed, fields eligible, audit retention)?
3. What are the precise UX priorities and MoSCoW ordering across the proposed improvements (bulk SIF, exports, search/filter, file indicators, layout changes)?
4. Should conclusion gating be hard-blocking until Data Admin sign-off, or can overrides be permitted under certain roles/conditions?
5. What security testing (e.g., vulnerability scanning, pen testing) is required and by whom; what is the schedule and acceptance criteria?
6. Are there performance targets (e.g., page response times, upload/processing times) and concurrent user expectations beyond 50–100 users?
7. What is the exact user concurrency/edit conflict resolution model for multi-user collaboration on active tests?
8. What export formats (Excel, PDF) are required for SIF and one-pagers, and what templates should be used for PPT generation?
9. What data validation rules must be enforced pre-save (mandatory fields, allowed values) for each SIF section and reference table?
10. What monitoring/observability tooling is preferred for availability and performance alerting, and who owns it operationally?
11. Any regional data privacy or retention requirements for vendor-submitted data and consumer responses?
12. When should SAP/Coupa integration be scheduled (phase 3) and what objects (vendor master, PO) are in scope for that integration?

# # 15. Source Notes

- Primary notes used: INPUTS_TEXT (Meeting transcript: RnD Sensory – Roadmap Discussion – 2025-05-30).
- Brownfield notes used: Final Sensory Workflow – Flow Diagram.pdf.

## Appendix: Phase 2 Feature Prioritization (MoSCoW)

| Feature | Priority |
| --- | --- |
| Pre-RFP approval and vendor update propagation | High |
| Post-completion data editability (Data Admin) | High |
| Improve Data Transformation Engine accuracy | High |
| Conclusion gating until transformation sign-off | High |
| Non-product test accommodation (no SIF path) | High |
| Multi-user collaboration on active tests | High |
| Contextual dropdowns (e.g., packaging types) | High |
| Bulk SIF copy/paste | Medium |
| SIF export (Excel/PDF) | Medium |
| Improved search/filter for completed tests | Medium |
| Clear file upload visibility indicators | Medium |
| Layout improvements to reduce scrolling | Medium |
| Study name auto-population and admin approval | Medium |
| Admin management of holding protocol tables | Medium |
| One-pager PPT download from fields | Medium |
| Generate McCain report template (PPTX) | Medium |
| SAP/Coupa integration (vendor/PO) | Future (Out of Scope Phase 2) |
| Predictive analytics enablement | Future (Out of Scope Phase 2) |