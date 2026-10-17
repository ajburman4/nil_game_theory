# PROJECT_BRIEF.md

## The NIL Arms Race: A Multi-Sport Athletics Investment Strategy Lab

**Brief prepared:** October 17, 2026 (America/Phoenix)  
**Audience:** Codex implementing the project; athletic directors, athletics strategy and finance leaders, and hiring managers reviewing the results.  
**Purpose:** A compact, credible research portfolio project for GitHub, GitHub Pages, LinkedIn, and college athletics job applications. This document specifies future work; it contains no completed empirical findings.

## 1. Mission and decision question

Build an explainable decision-support framework answering:

> How should a university allocate its discretionary athletics resources across sports, athlete compensation, coaching, and program support, given its institutional objectives and competitors' decisions?

Study the department as a portfolio. Football matters, but must not become the whole project. Compare performance relative to resources and expectations, particularly for schools with smaller budgets. Identify when specialization, balance, coaching investment, athlete compensation, or retaining budget is attractive under explicitly stated assumptions.

The finished story must distinguish three things: what historical data show, what the simulation assumes, and what decisions follow conditionally. An inconclusive empirical result or a scenario without a stable equilibrium is a valid finding. Do not force an arms-race narrative.

### Required outputs

1. An executed, explanatory Jupyter notebook and readable HTML export showing the analysis in steps.
2. An auditable data pipeline, source register, data dictionary, assumptions register, model documentation, and meaningful validation.
3. A static, self-contained `docs/index.html` strategy simulator, runnable locally and suitable for GitHub Pages.
4. A concise executive research brief, three publication-quality figures, a GitHub README, and a draft LinkedIn post grounded in actual findings.

Do not publish, deploy, or post publicly unless the user requests it. Prepare everything for review first.

## 2. Non-negotiable instructions for Codex

- **Never invent data, source URLs, quotations, article contents, coach salaries, NIL payments, budgets, legal provisions, findings, or statistical significance.** Do not convert a plausible number into a sourced fact.
- Mark every input as `observed`, `reported_estimate`, `derived_estimate`, `scenario_assumption`, or `proposed_policy`. A disclosure is observed as a disclosure; it is not necessarily independently audited truth.
- Keep missing values missing. Distinguish zero, not sponsored, not applicable, suppressed, unavailable, and unknown. Never silently substitute zero or a peer average.
- Maintain separate empirical and scenario datasets. Synthetic fixtures are allowed only in clearly labeled tests or demonstrations and must never enter research tables or named-school facts.
- Prefer public official data where reuse permits. Public visibility does not establish permission to scrape or redistribute. Record access and redistribution rights separately.
- Do not bypass paywalls, authentication, access controls, rate limits, or copyright restrictions. Do not reproduce articles, proprietary tables, or reconstructed paywalled datasets in the repository.
- When blocked on a source, record the gap, use an authorized alternative, and continue independent work. Ask only for information that is necessary to resolve a consequential gap. Do not present blocked work as finished.
- Use simple, interpretable baselines before adding complexity. Explain every transformation, model choice, parameter, and consequential fallback.
- Do not claim causal NIL returns from historical general-spending correlations. Do not use current estimates to explain earlier seasons as if known then.
- Never label a nonconverged numerical result a Nash equilibrium. Never describe the coaching-efficiency scenario input as a competitive shock.
- Preserve the user's holistic scope. Do not silently reduce the project to football or substitute Streamlit, a server, cloud functions, or live API calls for the static simulator.

## 3. Policy verification and accounting boundaries

### Dated policy checkpoint

As of **October 17, 2026**, treat the **Protect College Sports Act of 2026, S. 4668 (119th Congress), as Senate-passed proposed legislation, not enacted federal law**. The official Senate record shows passage on September 28, 2026, 77–22. GovInfo provides the Senate-engrossed text. October 16 reporting still describes the bill as awaiting an uncertain House outcome. Congress.gov's live bill/actions pages were inaccessible during preparation of this brief; do not imply that they were inspected successfully. [Official Senate vote](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00250.htm), [GovInfo version record](https://www.govinfo.gov/app/details/BILLS-119s4668es), [AP, October 16](https://apnews.com/article/e7a9026e4f3a260ba8735de4afa65027).

In the Senate-engrossed proposal, §114(a)(2) permits up to **$22.5 million per academic year above the revenue-share cap** to retain athletes with at least one full competitive season at that institution. Up to **$5 million more** is conditional on proportional compensation for non-revenue programs, including women's and Olympic sports. Academic benchmarks and a nine-year limitation apply; §115 addresses continuation. This is proposed payment capacity, **not federal funding or guaranteed school revenue**. Do not use older draft dollar amounts. [Senate-engrossed text, §§114–115](https://www.govinfo.gov/content/pkg/BILLS-119s4668es/xhtml/BILLS-119s4668es.html).

The House settlement is a court-approved settlement framework, not an act of Congress. NCAA implementation legislation defines a benefits pool/cap covering additional payments and benefits. The historical 2025–26 starting cap was approximately $20.5 million; it is not a permanent annual constant. Confirm the selected year's amount and counted benefits before using it. [NCAA adopted benefits-cap legislation](https://web3.ncaa.org/lsdbi/search/proposalView?id=108597), [NCAA implementation Q&A](https://ncaaorg.s3.amazonaws.com/governance/d1/legislation/2024-25/June2025D1Gov_PhaseThreeInstSetQuestionandAnswer.pdf), [AP settlement approval](https://apnews.com/article/4355c0db8bb2eaa4248650594f157053).

### Implementation rules for policy scenarios

Create `policy_status.md` and a machine-readable policy register. Before analysis and again before release, verify official bill actions, latest text, enactment/public-law record if any, effective dates, court orders, NCAA/College Sports Commission implementation, and applicability. Use [Congress.gov bill actions](https://www.congress.gov/bill/119th-congress/senate-bill/4668/all-actions), GovInfo, and official implementation documents. Record access failures and conflicting versions. An enactment clause or the words “AN ACT” on an engrossed bill are not proof of enactment.

Each policy record needs `as_of_date`, jurisdiction, authority type, bill/rule identifier, text version, section, status, source URL, retrieval date, effective period, applicable institutions, interpretation, and unresolved questions. A legislative change after this brief must update the register and UI, not silently overwrite the historical checkpoint.

Support three clearly named modes:

| Mode | Required treatment |
|---|---|
| Current framework | Only verified effective settlement/rule/legal constraints for the chosen year and participating school. Proposed retention exception is off. |
| PCSA proposal scenario | Separate opt-in, prominent “proposed policy” badge, pinned text version, funding source, eligible retained-athlete pool, and caveats. |
| Custom hypothetical | User-defined capacity or retention assumption with no claim of legal availability. |

Model a retention allowance as relaxing a payment constraint, not increasing available cash. Spending must still fit the school's funded budget. Maintain a baseline retain-versus-recruit allocation within verified existing payment capacity; an institution's retention strategy does not itself require the proposed additional allowance. Never add retained athletes' payments twice.

The conditional additional allowance must not become an unconditional $27.5 million slider. Implement only a documented interpretation supported by applicable guidance; until the proportional calculation is clear, disable that increment in the policy-faithful mode and allow it only as a labeled hypothetical. Do not claim that an extra dollar of spending guarantees retention. Retention response parameters are assumptions unless supported by suitable longitudinal evidence.

Review any proposal's implications for associated entities, third-party NIL, funding restrictions, participation protections, and implementation timing before combining levers. Do not cherry-pick increased capacity while ignoring linked restrictions. Do not automatically keep all current external NIL additive in a different policy regime.

### Separate money ledgers

Keep institutional athlete payments, counted noncash benefits, external NIL, coaching/staff, other operations, scholarships, capital/debt, and institutional subsidies separate. Separate school-controlled cash from external resources. External NIL is neither school revenue nor a school-controlled spending decision in the base model. Explain whether a report describes budget capacity, commitments, guarantees, cash paid, or total roster resources.

Reconcile mutually exclusive components to source totals. NCAA financial reports, EADA disclosures, and other databases may use different definitions; do not add overlapping figures or force them to agree. Revenue including transfers/subsidies is not independently generated revenue, and allocated sport revenue is not marginal revenue from winning.

## 4. Scope and feasibility gates

### Target research panel

- Public NCAA Division I institutions, with public FBS, FCS, and non-football coverage where comparable data exist. Private schools may be contextual examples only unless financial comparability is demonstrated.
- Start with academic seasons 2017–18 onward; choose the final historical window after auditing actual financial and performance releases. Use complete comparable seasons, not an assumed availability date. Keep 2026 estimates in a separate contemporary snapshot; the 2026 football season is incomplete on the brief date.
- Target 40–80 schools and six or more comparable seasons. Publish inclusion/exclusion rules and counts before modeling.
- Detailed target sports: football, men's basketball, women's basketball, baseball, softball, and women's volleyball. Keep gender designations explicit. Account for all remaining varsity sports through department totals, sponsorship/participation counts, protected budget commitments, and supplementary broad-success measures.
- Model an “other varsity sports” budget reserve, but do not treat heterogeneous sports as one literal competitive league. Aggregate underlying sport results only when compatible; otherwise show descriptive breadth measures.

### Minimum useful release

Aim for at least 30 institutions, five comparable seasons, and four detailed sports including at least two women's sports, plus the remaining-department reserve. Football can have a different supported subset. Report sport-specific sample sizes; do not require a balanced panel if that would discard most relevant schools.

If coverage misses this gate, document it and produce a clearly scoped pilot with transparent uncertainty. Do not claim the full empirical release is complete. Keep multi-sport scenario functionality even if some sport responses remain explicitly illustrative. The number of observations must justify model complexity; reduce covariates before inventing coverage.

Exclude individual athlete valuations, contractual advice, precise recruiting-market forecasts, endogenous conference realignment, stochastic disruption events, and a comprehensive facility construction optimizer from version 1. Account for fixed facility/debt commitments; treat new capital projects as an extension.

## 5. Data acquisition and provenance

The following are starting points, not a claim that every field or year has been acquired or licensed.

| Source | Intended use | Acquisition and limitations |
|---|---|---|
| [EADA](https://ope.ed.gov/athletics/) and [download portal](https://ope.ed.gov/athletics/public/html/datafile/datafile.list.html) | Team expenses/revenues, participation, sponsored sports, available coaching measures | Primary multi-sport financial foundation. Read each year's dictionary: team operating/game-day expenses are not total team expenses; aggregate coaching salary measures are not individual coach pay. Archive versions and reporting periods. |
| [Knight–Newhouse](https://knightnewhousedata.org/about) | Department finance, revenue sources, subsidies, available expense categories | Public DI financial context based on NCAA reporting. Verify export/reuse permissions and category definitions. Do not assume external NIL or complete post-settlement payments are included. Do not treat its entire department expense as discretionary cash. |
| Official university NCAA financial reports, EADA reports, audited statements, budgets and coach contracts | Reconciliation and named-school context | Use public institutional records and cite report/page/year. Budgeted and actual figures differ. Do not request nonpublic records or fabricate contract terms. |
| [NCAA statistics](https://stats.ncaa.org/) and official school/conference results | Outcomes, schedules, championships, coach history | Check permitted retrieval and historical completeness. Manual bounded collection is acceptable when automation is disallowed. Log canceled seasons and postseason-rule changes. |
| [NACDA Directors' Cup](https://nacda.com/sports/2018/7/17/directorscup-nacda-directorscup-html.aspx) | Supplementary department-wide achievement | Archive year-specific scoring and final standings. Sponsorship breadth, mandatory sports, and postseason access affect points. It is not a neutral universal measure or the sole optimization objective. |
| [CollegeFootballData documentation](https://api.collegefootballdata.com/getting-started), [coverage](https://api.collegefootballdata.com/data-availability), [terms](https://collegefootballdata.com/terms) | Football games, schedules, recruiting/talent and ratings if authorized | Optional enrichment. Verify current access, metric availability, and redistribution rights. API keys stay in environment variables, never in notebooks, HTML, or Git. Use official results as a fallback. |
| [IPEDS](https://nces.ed.gov/ipeds/use-the-data) | UNITID, applications, admissions, enrollment, tuition, institutional traits and finances | Use survey-specific definitions and dictionaries: HD, ADM, EF/E12 and appropriate finance files. Record provisional/final status. Institution admissions scope and reporting lags differ. |
| [BLS CPI](https://www.bls.gov/cpi/data.htm) | Inflation adjustment | Choose and document one annual index, base year, and fiscal-year mapping. Preserve nominal values for reconciliation. |
| USA TODAY coaching databases, official contracts/disclosures | Coaching compensation | Optional corroboration subject to access/reuse terms. Distinguish base salary, total compensation, incentives, assistants, buyouts, and year. Never impute head-coach salary from a department average. |
| [The Athletic roster-budget interactive](https://www.nytimes.com/athletic/interactive/college-football-nil-spending-budgets/) | Optional contemporary FBS football reported spending ranges | Candidate source identified from prior discussion and public references. Its original contents were not accessible during brief preparation. Verify original date, methodology, coverage, and meaning before using any numbers. Do not bypass access or commit its table. |

For The Athletic, the project must work without access. If the user supplies lawfully accessible material, record its exact source and what it measures. Publication of a range does not make it an audited payment or establish redistribution rights. An apparent combined roster budget cannot be relabeled external NIL; do not subtract a guessed institutional amount to manufacture a precise external estimate. Publish only permitted summaries/derived outputs with attribution; if rights are unclear, omit the restricted inputs from public artifacts and provide acquisition instructions. Never substitute an archive/paywall mirror.

### Required data artifacts

- `data_sources.csv`: source ID, publisher/title, original URL, publication and retrieval dates, source period, fields, units, coverage, access method, rights/terms URL, raw redistribution permission, derived-output permission, transformations, checksum, and limitations.
- `data_dictionary.csv`: definition, unit, status/type, period, source, denominator, missing codes and transformation for every model field.
- `institution_crosswalk.csv`: stable project ID, IPEDS UNITID, source-specific IDs, campus, name variants, and year-specific conference/division/sport membership. Review ambiguous matches; do not merge system totals with a campus.
- Immutable, timestamped raw snapshots where permitted; restricted inputs in ignored local folders with documented reacquisition steps. An open code license does not relicense third-party data.
- Separate historical observations, contemporary reported estimates, derived modeling tables, and scenario configurations.
- A coverage/missingness report by school, sport, year, and field; reconciliation discrepancies and exclusions must be visible.

Every joined table must have explicit grain and uniqueness checks. Record `season`, `academic_year`, fiscal start/end, reporting year, publication date, and availability date separately. Map them explicitly. Data published after a prediction origin cannot be described as a deployable historical forecast input; distinguish retrospective association analysis from real-time forecasting.

## 6. Tiered external NIL assumptions

Define external NIL as resources paid by noninstitutional parties under the selected regime. Separate associated/collective funding from independent commercial deals when definitions and coverage permit. Do not equate social-media valuation, collective fundraising targets, contract headline amounts, or total roster budgets with annual external payments.

Use this **illustrative, editable scenario grid only**. These are deliberately broad test ranges, not researched estimates of the market, percentiles, or classifications of named schools. Dollar units are nominal USD millions per department per academic year; set the scenario year explicitly.

| Scenario tier | Low | High | Meaning |
|---|---:|---:|---|
| Zero external funding | 0 | 0 | Counterfactual benchmark |
| Limited | 0.1 | 1 | Small external-resource scenario |
| Moderate | 1 | 5 | Intermediate test range |
| Substantial | 5 | 15 | Larger test range |
| High | 15 | 30 | High-resource test range |
| Very high | 30 | 50 | Stress-test range; custom values may exceed it |

Unknown is a separate state, not a tier. Numeric boundaries are scenario controls, not rules for classifying observations. Do not assign a real university to a tier without supporting evidence and explicit estimate labels. Generic archetype presets may use these ranges but must show “illustrative external NIL assumption.” For unknown schools, show the full sensitivity grid instead of a factual point estimate.

Specify a sport allocation vector summing to one, plus uncertainty in that vector. Never automatically allocate everything to football or divide equally. A football-only reported range stays football-only and cannot stand in for department-wide external NIL. Show how changing women's-sport allocations affects results.

For deterministic comparisons use low/mid/high values, with the midpoint labeled a convenience assumption. If Monte Carlo is useful, use a stated uniform or triangular scenario distribution, a fixed seed, and alternative shapes; a chosen distribution is not evidence. Allow correlated high/low external funding across rivals and correlation with institutional resources rather than pretending all draws are independent.

Hold external funding exogenous in the base game. Include separate sensitivity cases in which external support substitutes for, complements, or is independent of institutional payments. A school cannot costlessly control donor budgets. Make the effectiveness weight mapping external NIL to competitive resources explicit; it is calibrated/assumed unless estimated from credible comparable data. Do not reuse a general athletics spending coefficient as an identified NIL coefficient.

## 7. Hypotheses and analysis plan

Record hypotheses, primary metrics, specifications, peer definitions, exclusion rules, and validation splits before interpreting results. Use two-sided uncertainty where appropriate; report null and contrary findings. Treat these as association tests unless a separate causal design earns stronger interpretation.

| Hypothesis | Concrete comparison or test | Evidence standard |
|---|---|---|
| H1: Peer-relative resources add explanatory/predictive value | Compare absolute-spending model with absolute plus leave-one-out peer-relative spending; same outcomes, observations, covariates and validation folds | Held-out MAE/RMSE or log loss, school-cluster bootstrap uncertainty, and interpretation of collinearity. Relative and absolute spending are not independent treatments. |
| H2: Marginal returns diminish | Compare linear, log and low-complexity spline forms; inspect fitted marginal slopes across supported spending range | Derivative/contrast intervals and held-out fit, not curvature assumed by choosing a log function. Report insufficient evidence if unsupported. |
| H3: Strategic competition can be inefficient | Compare individual best responses/equilibrium with a planner benchmark under identical feasible budgets and declared utility | Simulation result conditional on payoff assumptions; report utility differences and equilibrium diagnostics. Do not frame as an empirical causal hypothesis test. |
| H4: Preferred allocations differ by institutional profile | Vary sport strengths, weights, budgets, coaching effectiveness and external NIL; compare allocations and regret | Stable differences across reasonable parameter ranges; avoid overfitted subgroup significance claims. |
| H5: Athletics success relates to broader institutional outcomes | Model subsequent applications, enrollment and available athletics revenue with school/year effects, lags and controls | Effect sizes/intervals, negative or null results, timing checks and alternative trends. Applications, yield and enrollment are separate outcomes. |

Use a small, declared primary family of tests; report multiplicity adjustments (e.g. Benjamini–Hochberg) for exploratory cross-sport coefficient screens. Do not fish across specifications for a LinkedIn headline.

### A. Outcomes and performance relative to expectations

Use sport-specific primary outcomes: schedule-adjusted regular-season win percentage where valid; separately report postseason qualification/progression. For sports with different schedules or formats, define defensible comparable outcomes rather than pooling raw win counts. Use completed season data and verified denominators. Document ties, canceled games, tournament expansion and selection changes.

Construct two expectation benchmarks:

1. A contextual benchmark using prior performance, competition, institutional context and other information available before the season.
2. A resource-adjusted benchmark adding measured spending and coaching inputs.

Their residuals answer different questions. Resource-adjusted residuals describe over/underperformance given resources; they cannot alone measure the total benefit of spending. Compute residuals out of sample and show uncertainty/shrinkage. Rank only where coverage supports comparison; avoid declaring a coach or school “best” from one noisy season.

Normalize outcomes within sport using training-period parameters. Show department scores under both equal-sport and explicit institution-priority weights, with coverage and sponsorship counts. Do not reward nonparticipation by dropping difficult sports from the denominator. Directors' Cup is a supplementary benchmark; [NACDA's 2025–26 description](https://nacda.com/news/2026/6/9/directorscup-grand-valley-washu-and-cumberlands-secure-learfield-directors-cups.aspx) illustrates why year-specific countable-sport rules matter.

### B. Historical resource and coaching models

Start with prior-season and peer-mean baselines, then sport-specific interpretable panel regressions. Candidate terms include lagged real spending, prior outcomes, schedule/competition strength, coach tenure, institutional resources and season effects. Explain selection with a small causal diagram, particularly whether recruiting/talent is a mediator of spending. Fit specifications with and without potential mediators; do not call a controlled direct association the total spending effect.

Use school effects where feasible; compare conference-year or peer controls without mechanically absorbing every relative-spending signal. Handle realignment with year-specific membership. Report when identification comes mostly from between-school versus within-school variation. Begin with separate sport models; introduce partial pooling/hierarchical models only if samples and validation justify it. Missing expenditure detail requires a coarser model, not invented decomposition.

Coaching spending and coaching quality are distinct:

- Measure compensation/staff investment from documented, nonoverlapping fields. Include assistants only when measured. Model annual buyouts as separate one-time commitments.
- Estimate a **coaching-effectiveness proxy**, not intrinsic coach quality, from prior out-of-sample resource-adjusted performance. Use rolling histories, shrink small samples toward a sport mean, show uncertainty, and use no target-season results.
- If a coach changes institutions, use only prior information and retain program-context controls. Missing coach histories receive an explicit prior/unknown label.
- Salary can follow success and residuals contain luck, player talent and unmeasured support; neither salary nor residuals isolate causal coaching skill.
- Optional salary-by-effectiveness interaction requires adequate data and out-of-sample improvement. Avoid counting the same measured coach effect both in baseline strength and an added scenario multiplier.

### C. Broader institutional outcomes

Use subsequent IPEDS applications, first-time enrollment and relevant demand/yield measures; add observed donation/revenue outcomes only if definitions are comparable. Account for institution size, admissions policy, demographic/geographic trends and pandemic disruptions where possible. Applications are not students, and tuition sticker price is not marginal net tuition contribution. Selection capacity can limit enrollment responses.

Historical relationships are exploratory. If causal identification is inadequate, keep institutional benefits as normalized utility scenarios with a default zero monetized benefit. Do not translate a win into invented tuition dollars or claim athletics generated enrollment growth. Avoid counting the same donation or brand pathway in several utility terms.

## 8. Transparent optimization and game theory

### Decision variables and feasible budget

For school `i`, sport `s`, choose incremental institutional athlete payments `a[i,s]`, coaching/staff `c[i,s]`, and discretionary program support `o[i,s]`. In a retention-enabled model split `a` into recruitment/new-player and eligible retention components; their sum remains one institutional payment ledger. External NIL `e[i,s]` is an input, not a school decision.

Define `B[i]` as genuinely available annual discretionary cash after fixed commitments and protected operating/participation needs. Require:

```text
sum_s (a[i,s] + c[i,s] + o[i,s]) + reserve[i] <= B[i]
a, c, o, reserve >= 0
```

Add sport floors, annual change limits, contractual commitments, protected other-sports budgets and verified payment/benefit caps. Do not subtract fixed costs twice. Separate the institutional cash constraint from the benefits-cap accounting constraint, which can count noncash benefits. A reserve/outside option is essential: the model must be able to recommend spending less than capacity.

Use participation and equity safeguards supported by current sources. Do not assert that a simple spending split proves Title IX compliance or that a fabricated percentage is legally required. Version 1 protects existing sports rather than recommending sport elimination. Scenario floors may exceed legal minima; label them institutional assumptions.

### Response functions and competitive outcomes

First expose a one-school, two-sport worked example with every input and intermediate value. Use a documented, bounded mapping from incremental resources to sport strength, such as:

```text
F(A,C,O,E,q) = betaA[s] * log(1 + A / scaleA[s])
             + betaC[s] * q * log(1 + C / scaleC[s])
             + betaO[s] * log(1 + O / scaleO[s])
             + betaE[s] * log(1 + E / scaleE[s])

z[i,s] = baseline_strength[i,s]
         + F(A0+a, C0+c, O0+o, e, q)
         - F(A0,   C0,   O0,   E0, q0)
```

Here `A0,C0,O0,E0,q0` are the declared baseline resource levels and effectiveness for that school/sport; `e` and `q` are scenario levels, while `a,c,o` are increments. Baseline strength is calibrated at those same baseline inputs. This difference formulation prevents counting existing resources twice and lets improved coaching effectiveness matter at an unchanged, positive existing salary budget.

This is a candidate scenario form, not a finding. All scales must be positive and use consistent dollar units; effectiveness uses a documented positive scale. Baseline resource components must be sourced or labeled assumptions, not fabricated decompositions. If historical spending is inseparable, calibrate only a combined resource response and label category splits/elasticities assumed. Do not infer four coefficients from one observed total.

Provide linear/saturating alternatives. Diminishing resource-to-strength returns do not guarantee diminishing returns in every region of the final probability function. Clip or constrain unsupported extrapolation and display the boundary.

For head-to-head sports a simple interpretable contest mapping is:

```text
p(i beats j in sport s) = 1 / (1 + exp(-(z[i,s] - z[j,s])))
expected_win_fraction[i,s] = weighted mean of p(i beats j)
```

Use actual or explicitly hypothetical schedule weights. Validate paired probabilities sum to one. This proxy is not a national-title probability. Title/postseason probabilities need a separate validated tournament model; omit them if unsupported. For track/individual/team-meet sports use compatible rankings/descriptive outcomes rather than forcing a head-to-head formula.

Define competitive sets by sport: conference/schedule peers, supplemented by documented national comparators where relevant. A small modeled game omits most opponents; include fixed outside opponents or a documented outside-field strength. Do not award the entire national championship to a five-school illustrative game.

### Utility and opportunity cost

Use normalized utility, for example:

```text
U[i] = sum_s w[i,s] * normalized_performance[i,s]
       + lambda[i] * normalized_incremental_athletics_value[i]
       + gamma[i] * normalized_institutional_value[i]
       - kappa[i] * discretionary_spending[i] / B_reference[i]
```

Fix normalization anchors before scenario comparison, define all weights and keep the reference budget positive. Do not restandardize each scenario in a way that changes its utility scale. State whether the cost term represents cash, opportunity cost, or risk; avoid subtracting the same cost again inside a net-revenue term. Show a Pareto frontier across competitive success and sustainability instead of pretending weights are objectively correct. Include budget reserve utility if used and explain its relationship to the cost penalty.

Value weights reflect user-defined institutional priorities, not revealed university preferences. Do not sum raw wins, dollars and students. Financial/institutional submodels can be omitted from a core fit when unsupported, while retaining clearly labeled user-assumption controls.

### Games and equilibrium diagnostics

1. Demonstrate best response for one institution against fixed opponents.
2. Build a two-school/two-sport finite-grid example; enumerate feasible actions and check unilateral deviations directly.
3. Extend to a small, explainable game of 3–6 representative competitors. Use damped sequential best responses, multiple starts and a finite iteration limit. Record solver method, action resolution, constraints, update order, seed and tolerances.
4. Compute each school's regret: best achievable unilateral utility minus utility at the candidate profile. Report maximum regret and the accuracy of the best-response search. Use a declared tolerance, initially `epsilon = 0.001` on the fixed normalized utility scale, with sensitivity checks.
5. Label results “approximate equilibrium on the stated action grid” only when the regret check passes within search accuracy. A small change between iterations is insufficient. If best responses are approximate, state the bound/limitation. Report cycling, multiple solutions or failure to converge honestly.
6. Compare with a numerical planner benchmark maximizing the same aggregate utility under the same feasible resources and outside opponents. Call it a benchmark, not a recommendation for schools to coordinate compensation.

Do not assume a unique pure equilibrium exists. Bound computation for browser use; show resolution tradeoffs. Never report planner utility below a feasible equilibrium without investigating optimization failure. Use utility differences rather than an efficiency ratio when utilities can be zero or negative.

Competitions redistribute wins; institutional benefits need not be zero-sum. With fixed exhaustive budgets and purely relative success, a manufactured “overspending” result is easy to bake in. Allow reserve decisions and opportunity costs, and demonstrate counterexamples in which the inefficiency disappears. Quantify athlete compensation separately: university utility is not total social welfare, and lower athlete pay is not automatically a social improvement.

### Competitor coaching-efficiency scenario

Expose **“Competitors' coaching efficiency improvement”** as a percentage input, selectable by rival and sport or common to all rivals. Apply it to the rival coaching-effectiveness term, holding salary fixed unless the salary lever changes separately. Define a positive reference effectiveness scale so a 10% improvement cannot accidentally worsen a negative residual. Show the baseline and improved values and recompute best responses/equilibrium.

Use illustrative improvements of 0%, 5%, 10% and 20% for sensitivity, not empirical predictions. Explain that schools may obtain more competitive value from the same coaching expenditure. Include a separate competitor-spending lever. No generic disruption or shock engine is required.

## 9. Real-university archetypes with evidence and restraint

Use these as contextual case studies, not rigid categories or endorsements. They overlap. Recheck facts and sport sponsorship before implementation. School identities do not supply missing budgets, NIL estimates, priorities or coefficients. An illustrative preset inspired by a school must say so beside the school name; otherwise offer a generic profile.

| Archetype / university | Evidence-based context | Modeling question and caution |
|---|---|---|
| Large-resource football contender — **The Ohio State University** | The university reported record FY2025 athletics revenue after its football championship season. [Official financial release](https://news.osu.edu/ohio-state-athletics-sets-record-with-336m-in-fy25-revenue-after-national-championship-season/); [institutional disclosures](https://ohiostatebuckeyes.com/sports/2018/6/1/certifications). | Compare football investment with department breadth and reserve. Reported total revenue is not discretionary cash or an NIL budget; championship-year receipts may be atypical. |
| Broad multi-sport contender — **UCLA** |  | Explore balanced sport priorities and existing strengths; account for Cup scoring rules. A finish does not establish the best spending allocation. |
| Basketball-centered scenario — **University of Connecticut** | UConn's FY2025 financial report release records its 12th women's basketball national title and other sports' results. [Official report release](https://uconnhuskies.com/news/2026/1/15/general-uconns-annual-ncaa-financial-report-released). | Give men's and women's basketball separate priorities while retaining football and other sports. Do not infer institutional objectives from championships or assume basketball finances eliminate subsidy questions. |
| Football challenger — **Boise State University** | Boise State earned a No. 3 seed and bye in the 2024 College Football Playoff. [Official announcement](https://broncosports.com/news/2024/12/8/boise-state-earns-fiesta-bowl-berth-no-3-seed-in-college-football-playoff). | Test targeted investment and performance versus resources. Establish relative budget size from actual financial data; verify conference membership by season rather than projecting a historical label forward. |
| Visibility and institutional-demand scenario — **Florida Atlantic University** | Its men's basketball program reached the 2023 Final Four. [Official announcement](https://fausports.com/news/2023/3/27/mens-basketball-florida-atlantic-to-the-final-four-gear-travel-ticket-info). | Examine subsequent demand measures and alternate visibility weights. This event neither proves an enrollment effect nor establishes “enrollment-focused” as FAU's official strategy. |

For each case card show source-year facts, coverage, chosen assumptions, feasible budget construction, competing objectives, results versus baseline, and the conditions under which the recommendation changes. Include resource-efficient schools identified by the analysis even if they differ from these examples. Named schools must not receive fabricated “optimal NIL budgets.”

## 10. Notebook: show the work, step by step

Use `notebooks/01_research.ipynb` as the main narrative. Keep reusable functions in `src/`, but do not bury core equations or transformations inside opaque helpers. Include small displayed intermediate tables and a hand-checkable worked example.

Required sequential sections:

1. Decision question, intended audience, hypotheses, scope, evidence labels and dated policy checkpoint.
2. Environment, package versions, seed, configuration, data snapshot dates and rights summary.
3. Data acquisition manifest and actual coverage; explicit unavailable sources.
4. Institution/season mapping, cleaning, inflation, definitions and reconciliation checks.
5. Descriptive department portfolio and spending distributions, with missingness and women's-sport coverage.
6. Outcome construction and contextual/resource-adjusted expectation models.
7. Spending response comparisons, coaching proxy construction and leakage checks.
8. Institutional-outcome analysis or a candid explanation of why it remains exploratory.
9. External NIL tier scenarios and uncertainty, clearly separated from historical inference.
10. One-school allocation example, two-school game and equilibrium/regret checks.
11. Archetype comparisons; competitor coaching-efficiency and policy scenarios.
12. Robustness, limitations, conditional findings, simulator export and executive implications.

For **every analytical step**, include markdown explaining the question, inputs, units, choices, equation/logic, expected diagnostic, actual result, and interpretation limits. Display code followed by its executed output, then a brief “what this means” paragraph. Do not write findings before outputs exist. Every chart needs source/period, units, denominator, evidence class and an intelligible takeaway; distinguish scenario bands from statistical confidence intervals.

Restart the kernel and execute top to bottom in a clean environment. No hidden state, missing cells, manually fabricated output, or out-of-order execution. Record the exact command used for execution and HTML export. A reader should be able to trace each published number to a cell, input snapshot and configuration.

## 11. Static simulator specification

Deliver one generated `docs/index.html` containing all required CSS, JavaScript, permitted compact data, parameters and graphics. It must work via `file://` and GitHub Pages HTTPS with **no backend, Python runtime, Streamlit, CDN, remote fonts, live API, analytics, credentials, or runtime fetch of local JSON**. Use system fonts and native SVG/canvas or inline properly licensed code. Keep generation code and readable JS source in the repository even if the release artifact is bundled.

### Inputs

- Generic archetype or evidence-backed school context, with visible data vintage.
- Funded discretionary budget; sport/category allocation controls and protected commitments.
- External NIL tier/range and sport split for school and rivals, visibly labeled as assumptions.
- Coaching spending, own coaching effectiveness and competitors' efficiency improvement.
- Competitor budgets/spending, sport priorities, sustainability and institutional-value weights.
- Current framework, proposed PCSA scenario or custom policy mode, with policy date/version.
- Optional retention allocation and effectiveness assumptions; disabled where unavailable.

### Outputs and usability

- Baseline versus selected allocation; total, remaining/reserve and binding constraints.
- Sport performance proxies, uncertainty/sensitivity ranges and a success-versus-sustainability frontier.
- Best-response comparison and, where supported, approximate-equilibrium result with maximum regret, action resolution and convergence status.
- Marginal allocation tradeoffs; separate observed context, fitted relationships and assumed parameters.
- Plain-language explanation: what changed, why, and which assumptions drive it.
- Clear source, methodology, limitations and proposed-policy panels; persistent indication when a scenario is illustrative or outside empirical support.
- Reset, save/download scenario JSON, load validated JSON, and downloadable results CSV. Reject invalid values and unsafe/unsupported schema fields; do not execute imported content.
- Keyboard-accessible controls, associated labels, responsive layout, readable mobile charts, adequate contrast, and no information conveyed by color alone.

Keep the default view understandable with a small number of controls; put advanced assumptions in an expandable area. Choose descriptive labels such as “Modeled win fraction,” not “Guaranteed wins.” Display dollar amounts at a precision justified by inputs.

For speed, use bounded deterministic search or clearly marked precomputed scenario grids. If interpolating precomputed results, state the grid and interpolation limits and do not claim a freshly solved equilibrium. A visibly nonconverged result is preferable to a misleading success badge.

## 12. Validation, uncertainty, and risks

### Required checks

- Data: unique grain, joins and unmatched IDs, season/fiscal mappings, duplicate categories, missing versus zero, nonnegative costs, plausible units, supported sports and accounting reconciliation.
- Statistical: rolling-origin or blocked season holdouts; all preprocessing and coaching proxies fit using training history only. Keep final holdout untouched until model selection. Show performance against simple baselines; use school-clustered inference/bootstrap and sensitivity to common season effects.
- Robustness: pandemic exclusion and inclusion, alternative peers and realignment treatment, alternate outcome normalization, lag choices, model forms, imputation/exclusion choices and reported-estimate ranges. Report within-sport support and uncertainty at high spending levels.
- Optimization: budget and policy feasibility, sport floors, reserve option, scale invariance where expected, zero external NIL, flat resource returns, symmetric competitors, extreme priorities and no-football profiles.
- Game: analytically/enumerably check the tiny game; regret calculation, multiple starts, numerical precision, update-order sensitivity, cycling and max-iteration behavior. Separate optimizer error from parameter uncertainty.
- Policy: proposed retention allowance is zero in baseline; changing capacity without changing funded budget cannot create cash; ineligible retention is rejected; ambiguous conditional allowance stays disabled in policy-faithful mode.
- Cross-language: export Python reference scenarios and compare browser calculations to them, including probabilities, utility, allocations and constraints. Declare tolerances; use `1e-6` for deterministic scalar calculations where appropriate and grid-aware tolerances for allocations.
- Browser: local file and static-host modes, offline/network-disabled operation, responsive and keyboard behavior, invalid input handling, import/export round trip, no console errors or network dependencies. Target under two seconds for default interactions on a documented test device; degrade transparently if search is costly.

Tests must verify meaningful properties, not mirror implementation line for line. Distinguish model-parameter uncertainty, unknown external-NIL scenarios, policy uncertainty and numerical approximation. Scenario ranges are not automatically confidence intervals.

### Risk register and mitigations

| Risk | Required response |
|---|---|
| Reverse causality and omitted variables | State associational interpretation; show lagged and alternate specifications; avoid causal ROI labels. |
| Sparse post-settlement history and opaque NIL | Separate historical fit from current scenarios; range analysis; do not backfill unknown years. |
| Accounting heterogeneity and double counting | Source-specific definitions, reconciliation ledger, no forced synthetic equality. |
| Coaching selection and generated-regressor noise | Prior-only proxies, shrinkage, sensitivity and no claims of intrinsic skill. |
| Missingness/selection and survivorship | Coverage report, exclusion flow, public-school limits and alternative samples. |
| Pandemic, realignment and postseason changes | Explicit indicators/period handling and year-specific peer/scoring rules. |
| Unsupported utility and retention benefits | Visible weights, zero-benefit defaults where unestimated, counterexamples and sensitivity. |
| Policy changes or ambiguous interpretation | Versioned register, dated UI, effective-date checks; disable unsupported policy calculations. |
| Licensing or inaccessible journalism | Independent public-data path, no paywall bypass, no restricted public dataset or text reproduction. |
| Overstated social conclusions | Report university, athlete and participation outcomes separately; planner utility is not total welfare. |

## 13. Repository, implementation phases and review gates

Suggested structure (paths below are repository-relative specifications):

```text
PROJECT_BRIEF.md
README.md
requirements.txt or pyproject.toml + lockfile
config/                 # assumptions, peers, utility weights, policy versions
data/README.md
data/raw/               # only redistributable snapshots; restricted files ignored
data/processed/         # only permitted derived artifacts
data/data_sources.csv
data/data_dictionary.csv
data/institution_crosswalk.csv
notebooks/01_research.ipynb
src/                    # ingestion, metrics, fit, scenarios, optimization, export
tests/fixtures/         # clearly marked synthetic and reference scenarios
reports/policy_status.md
reports/assumptions_register.csv
reports/validation.md
reports/model_card.md
reports/research.html
reports/executive_brief.md
reports/figures/
reports/linkedin_draft.md
simulator/              # readable source and build/export scripts
docs/index.html         # standalone release artifact
```

### Phase 0 — Evidence and policy audit

Inspect repository instructions and existing files. Establish the source/rights register, policy checkpoint, definitions, season mapping and sample coverage. Confirm whether the Athletic source can be lawfully used. Produce a feasibility note and explicit gaps. **Gate:** know which questions can be empirical and which require assumptions before fitting anything.

### Phase 1 — Public-data foundation

Acquire permitted snapshots, build crosswalks, reconcile finance, produce descriptive plots and coverage tables. Freeze the hypothesis/validation plan. **Gate:** clean, traceable multi-sport panel and transparent exclusions; no modeled recommendations yet.

### Phase 2 — Explainable historical analysis

Execute notebook baselines, spending models, coaching proxies and institutional-outcome exploration. Compare supported specifications and document failed or inconclusive results. **Gate:** every takeaway is backed by executed output and appropriate evidence labels.

### Phase 3 — Strategy model

Build the hand-checkable example, finite-grid game, budget constraints, NIL tier sensitivity and coaching-efficiency scenarios. Add proposed-policy functionality only with versioned interpretation. **Gate:** feasibility and regret checks pass; uncertainties and unsupported elasticities remain explicit.

### Phase 4 — Static product

Export allowed parameters/reference scenarios and build the standalone simulator. Verify Python/JS parity, offline behavior, usability and accessible labeling. **Gate:** results are reproducible and the browser never implies stronger evidence or convergence than the notebook.

### Phase 5 — Portfolio release package

Re-execute notebook, refresh policy status, verify rights and numerical claims, write a 2–4-page-equivalent executive brief and concise README, export three figures and draft the LinkedIn post. **Gate:** user can inspect the complete local package before any requested public release.

Prefer a small coherent release over speculative sophistication. Optional extensions: richer hierarchical models, roster-level continuity if lawfully available, endogenized external funding, multi-year capital allocation and more sports. Do not let them block the core deliverables.

## 14. Acceptance criteria

The project is complete only when the applicable items are demonstrably satisfied:

- [ ] The stated question, hypotheses and department-wide scope survive through the notebook, strategy model and simulator.
- [ ] Public-data empirical analysis meets the minimum coverage gate, or the deliverable is prominently designated a narrower pilot with the unmet gate recorded.
- [ ] All named-school facts and published numerical claims have traceable source, period, units and evidence class; no fabricated observations or implied school endorsement.
- [ ] Every model field has a definition and provenance; source rights and restricted-data exclusions are documented.
- [ ] Historical observations, reported estimates, derived quantities, assumptions and proposed policies remain distinguishable in tables, charts and exports.
- [ ] External NIL tiers, sport allocations and substitutions are editable; unknown does not become zero or a factual tier assignment.
- [ ] Athlete payments, external NIL, coaching, operating costs, fixed commitments and counted benefits reconcile without double counting.
- [ ] Coaching salary and effectiveness are separate; the coaching proxy uses only prior information and rival efficiency improvement works at fixed salary.
- [ ] At least one resource-adjusted performance analysis highlights smaller-school context without treating noisy residuals as causal efficiency.
- [ ] H1/H2 receive actual model comparisons, H3/H4 are identified as conditional simulations, and H5 is exploratory unless a stronger design is established.
- [ ] Current policy mode excludes the proposed PCSA retention exception; policy status/version is dated, and no allowance is treated as free funding.
- [ ] The notebook runs cleanly from a fresh kernel with sequential executed cells, commentary, visible diagnostics and a readable HTML export.
- [ ] The small game is independently checked; any equilibrium label includes regret, tolerance, resolution and convergence information. Failure to find one is reported honestly.
- [ ] Allocation feasibility, protected other-sports funding, a reserve option, uncertainty, empirical-support limits and utility assumptions are visible.
- [ ] `docs/index.html` is genuinely self-contained and runs offline through both a local file and static hosting without server/CDN/API dependencies.
- [ ] Python/browser reference cases agree within declared tolerances; relevant data, model, optimizer and browser checks are recorded.
- [ ] Executive brief and LinkedIn draft contain actual results and material limitations, with no predetermined sensational finding.
- [ ] README gives exact acquisition, environment, notebook execution, simulator build and static preview instructions, including what is unavailable without restricted inputs.
- [ ] Code license, data permissions, attribution and policy citations are present; public artifacts contain no secrets, copyrighted articles or unlicensed tables.

## 15. First instruction to the implementing Codex agent

Start with Phase 0. Read repository instructions, inspect existing materials, and create the source/rights register, policy register, assumptions register and feasible data inventory. State the proposed historical cutoff and covered sports based on real availability. Then implement phases in order, updating the notebook narrative as results emerge. Continue useful independent work when one source is inaccessible. Bring consequential ambiguities to the user with the evidence and a concrete fallback. Do not claim completion until the acceptance criteria and material limitations are documented.
