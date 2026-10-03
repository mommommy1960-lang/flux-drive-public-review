# Aurora / Flux Drive — Research Progress Log

This public record reports completed research work and its evidence status. Detailed technical records are maintained separately in a private repository. Public entries omit unpublished mathematics, blueprints, device parameters, raw measurements, and enabling implementation details.

## Record policy

- Append a dated entry whenever substantive research, calculations, code, tests, corrections, or decisions produce a result.
- Preserve earlier entries, failures, and null results. Add dated corrections that identify the earlier statement.
- Credit external researchers and state the project's actual contribution.
- Distinguish reviewed literature, project calculations, simulation, planned experiments, measured results, and independent replication.
- Record remaining limitations and the next evidence gate. A research update does not itself validate a device.
- Entries document work when it occurs; this log does not claim unattended research runs every day.

## 2026-10-03 — motion, heat, distance, and evidence review

**Completed work:** six-worker review and integration covering public/private logging, optical motion models, thermal assumptions, distance limits, and spacetime-evidence boundaries. No physical experiment was performed in this review.

**Published-source findings:** Lorenzi, Salasnich, and Pelizzo's 2025 optical-cavity study models conventional lightsail propulsion with motion, delayed light returns, and wavelength-dependent mirrors. It identifies diffraction and redshifted-light heating as limitations. Its simulation uses idealized alignment and focusing; it is not a demonstrated spacecraft.

**Our contribution:** reviewed those assumptions against the proposed measurement program, distinguished stationary force comparisons from moving-spacecraft performance, and identified further model-accounting and applicability checks. Detailed audit notes remain private.

**Measurement evidence:** NIST's published photon-momentum instrument demonstrates that optical force measurements at hundreds of watts are possible. This is outside evidence; the project's proposed comparison remains unperformed and its instrument has not been independently certified.

**Spacetime evidence:** reviewed the distinction between ordinary light-pressure tests and physical warp-drive models. Published constant-velocity models leave creation of the required source and efficient physical acceleration unresolved. No new Flux-shell tensor result is claimed.

**Decision:** pursue a defensible conventional-physics comparison before interpreting any unexplained residual. The next modeling gate is whether recycled light still provides a benefit when motion, beam capture, spectral response, heat, and complete energy/momentum accounting are included.

**Current outcome:** no working Flux source, verified anomalous propulsion, faster-than-light result, or flight-capable Flux engine established.

### Credited primary sources

- F. Lorenzi, L. Salasnich and M. G. Pelizzo, [Optical Cavity in Relativistic Regime for Laser Propulsion](https://arxiv.org/html/2508.12442v1), 2025.
- A. Artusio-Glimpse and colleagues, [NIST: Miniature Force Sensor for Absolute Laser Power Measurements via Photon Momentum at Hundreds of Watts](https://www.nist.gov/publications/miniature-force-sensor-absolute-laser-power-measurements-photon-momentum-hundreds-watts), 2020.
- A. Bobrick and G. Martire, [Introducing Physical Warp Drives](https://arxiv.org/abs/2102.06824), 2021.
- J. Fuchs and colleagues, [Constant Velocity Physical Warp Drive Solution](https://arxiv.org/html/2405.02709v1), 2024, especially the acceleration discussion.

External papers and instruments remain credited to their authors. This entry records this project's review and decisions, and makes no claim to inventing those prior technologies.


## 2026-10-03 — finite-energy photon bookkeeping check

**Completed work:** an idealized numerical photon-packet calculation with independent closed-form checks. Five illustrative cases passed optical-energy, radiation-impulse, and mechanical-work consistency checks.

**Finding:** repeated reflections can redistribute a light packet's momentum between separate bodies. For a receding target, mechanical work draws down the packet's optical energy; the useful impulse from a finite-energy packet does not grow without limit.

**Limits:** the calculation prescribes the mirror motion. It does not simulate spacecraft acceleration, beam capture, propagation delay, thermal behavior, or a Flux shell. No physical force measurement or flight test occurred.

**Contribution and record:** this project performed the numerical bookkeeping check using conventional physics. Detailed equations, numerical cases, and the audit script are retained in the private record. Previous public entries remain intact.

**Next gate:** extend the comparison to moving trajectories and real optical losses without losing conservation or confusing pulse energy with circulating power.


## 2026-10-03 — causal photon travel and recoil audit

**Completed work:** a separate idealized numerical extension now follows photon travel time and finite-mass mirror recoil. Nineteen new tests cover analytic limits, conservation, causal encounter timing and losses; all 147 current tests passed locally. An independent code review supported the stated ideal bookkeeping. Detailed implementation and numerical evidence remain in the private repository's PR #29.

**Finding:** mirror separation changes subsequent light-travel times. Missed light must remain in the energy and momentum ledger. Reflections redistribute momentum between bodies, and mirror kinetic energy draws on optical energy or pre-existing mechanical energy. Comparison by bounce count alone is insufficient for a time-limited mission.

**Five parallel source reviews:** ten previously unlogged patent publications added control, tracking, thermal and calibration references. Credits: Schwemmer (US5184241A); Frankel/Pelekhaty (US12323199B2); Poon/Carden/Englekirk (US6522440B1); Ngo/Dixon/Schrier (US7366419B2); Mirtich/Sovey (US4199650A); Liu/Casse/Daniel/Afshinmanesh (US20170297750A1); Pais (US10144532B2); Pinto (US20070007393A1); Newbury/Coddington/Swann (US8558993B2); Cumpson (US7246513B2). Primary records are available at https://patents.google.com/ by publication number. The source proposals did not establish a usable warp field or inertial cancellation.

**Limits and corrections:** this project's contribution is numerical implementation, review and test planning, not invention of the cited technologies. An initially mistaken test expectation for approaching mirrors was corrected and preserved in the private history. No physical equipment, force measurement, cavity-locking demonstration, flight test or new Flux shell-energy result occurred. Legal-status labels are research leads; no freedom-to-operate conclusion is made.

**Next gate:** compare single-pass and recycled cases at equal injected energy and equal elapsed time, including all bodies and escaping light, then bound optical/thermal losses before defining a physical measurement. Earlier public entries remain unchanged.


## 2026-10-03 — hosted validation follow-up

The regular test workflow also passed all 147 tests. A separate repeated-validation workflow initially failed because its environment omitted NumPy, which existing tests require. After dependency setup was corrected on the research branch, all 100 validation jobs passed. These repeated software runs are not independent physical replications. The initial failure remains recorded. The private calculation PR is open for review; the public summary contains no enabling implementation details.


## 2026-10-03 — time-matched photon comparison and loss bookkeeping

**Completed work:** the numerical comparison now uses the same injected light energy and the same elapsed observation time for single-pass and recycled cases. Both platforms evolve freely. Missed and transmitted light retain their energy and signed momentum; absorbed light transfers momentum and increases stored mirror heat. Sixteen new analytic and conservation tests bring the locally passing suite to 163 tests. Detailed implementation and numerical cases are retained in private PR #29; hosted verification of this extension is pending.

**Finding:** repeated reflections can increase the impulse delivered to one separate platform, while losses reduce that advantage. Distance can prevent any return—or even the first arrival—within the observation interval. The complete two-platform-plus-light ledger closes; no unexplained net-system momentum is produced. A larger impulse on one mirror does not imply a working Flux source or additional energy.

**Limits:** loss fractions are illustrative bounds, not measured coating or pointing performance. Stored heat is included in energy accounting, but temperature, cooling, thermal deformation, diffraction, spectral response and cavity locking remain unresolved. The absorption/reflection interaction is a declared simplified ordering. No physical bench or thermal-survival test occurred. An approaching-mirror test initially exceeded the valid observation interval and hit the event guard; that rejected run and corrected interval remain recorded privately.

**Credit and contribution:** this project implemented and checked the time-matched numerical comparison under conventional energy and momentum conservation. External optical-propulsion, NIST metrology and patent references retain the author/inventor credits recorded above. No new patent screen or independent review of this extension is claimed.

**Next gate:** use traceable optical loss/capture inputs and add temperature/cooling dynamics with emitted-light momentum before defining a physical measurement operating point. Earlier entries and corrections remain intact. No new Flux-shell calculation, anomalous force, warp source or flight result is established.


## 2026-10-03 — comparison hosted verification

The regular GitHub test workflow for the comparison implementation also passed all 163 tests. Both the public summary and private detailed log were read back successfully, with earlier entries preserved. This verifies software execution under the stated assumptions; it is not independent physical replication, measured propulsion or a thermal-survival result. The private PR remains open for review.


## 2026-10-03 — independent internal review and numerical reliability

Five distinct research workers reviewed the equal-time conventional photon comparison, including causal timing, collision channels, thermal bookkeeping, numerical boundaries and independent analytic limits. This is internal software review, not external peer review or physical replication. The project found extreme-input cases that could silently erase a small impulse or give unreliable conservation diagnostics; the calculation now rejects those unsupported cases. Six additional regression and analytic tests bring the passing local suite to 169 tests. Hosted verification of this repair is pending. Detailed cases, rejected runs and implementation remain in private PR #29; earlier history is preserved.

The existing research watch now includes bounded numerical follow-up alongside patent screening. Its next measurable gate remains traceable optical inputs and thermal/cooling accounting, including the momentum carried by emitted light, before selecting a physical measurement. No new patent screen, shell-energy calculation, hardware result, warp source or flight is claimed. Prior inventor/source credits remain intact; this project's contribution here is review, correction and testing of its numerical model.


## 2026-10-03 — review repair hosted verification

The regular hosted workflow also passed all 169 tests for the reviewed numerical repair. Saved code and public/private progress records were read back successfully. This establishes software execution under the stated assumptions; no physical replication, warp source or flight is established. The research PR remains open for review.


## 2026-10-03 — thermal recoil accounting and new source review

A conventional isolated radiation-emission calculation now accounts for emitted-light momentum, mirror recoil and the associated loss of stored rest energy in different reference frames. Ten new analytic tests bring the locally passing suite to 179; a separate research worker independently passed the ten focused tests. Hosted verification is pending. This event calculation does not yet supply a temperature, cooling rate or time-coupled optical model. Earlier failed test expectations caused by decimal precision were corrected and preserved privately.

Five new bounded source tracks found useful cooling/metrology references and clear negatives: Boris Volfson (US6960975B1), Laurent G. Pilon (US20110298333A1), Marian Florescu/Jonathan Dowling/Hwang Lee (US20090217977A1), Denis Villate/Marco Soscia (US10228295B2), and Richard William Aston/Michael J. Langmack (US9403606B2; related Aston US9238513B2). Publication records are linked in the credited private source ledger. Their patent claims do not establish a warp source. One calorimeter's disclosed resolution is too coarse to establish the proposed low-heat measurement gate; angular radiation must be measured separately from total cooling. The new source records remain references or negatives, not installed hardware, and displayed status does not establish freedom to operate.

This project's contribution is source screening, conventional numerical accounting and software review, not invention of cited technology or physical replication. Primary thermal-recoil research credit: Turyshev, Toth, Kinsella, Lee, Lok and Ellis (2012), https://arxiv.org/abs/1204.2507 . Next: traceable thermal and angular-emission data, separate incoming-background accounting, then coupling to the causal photon comparison. Private implementation remains in PR #29. No new shell-tensor, bench, anomalous force, FTL or flight result is claimed.


## 2026-10-03 — thermal-event hosted verification

The regular hosted test suite passed all 179 tests for the new isolated thermal-emission calculation. Saved code, both progress records and the credited source ledger were read back successfully. This is software verification, not a cooling-rate measurement, physical replication or drive validation. The private PR remains open.


## 2026-10-03 — patent-inspired capture, cooling and power checks

Four new records were reviewed with inventor credit: Schuma/Teppo (US4846550A), Swanson/NASA (US6538796B1), Doiron/Paspa/Dunn (US5251004A), and Cole/Wittwer/Perner/Winkler/Mayer/Heckl/Follman (US12352987B2). The last coating family is active, so it is not expired art. A repeated propulsion candidate was excluded as already screened. Status/family labels remain unverified metadata, not freedom-to-operate conclusions.

The project implemented conventional Gaussian capture bounds, a restricted radiative cooldown timeline, and angular collection/momentum checks. A calculated capture fraction was tested in the existing finite-mass photon model for a first pass. Eleven new tests bring the passing local suite to190. A separate reviewer verified the original focused tests and found a tiny-angle numerical cancellation, now corrected with a regression. Hosted verification is pending. Detailed assumptions/results are private in PR29; earlier failures remain preserved.

The experiments show why missed light, thermal properties and detector collection angle must be explicit rather than presumed. They do not establish patented-device performance. No fabricated optics, thermal-survival measurement, general moving cavity, new shell source or flight is claimed. Source credit also includes Francesco D'Angelo/Edmund Optics for standard Gaussian equations and NIST CODATA for constants. Next: measured or bounded optical/thermal inputs, finite background heat, and a complete moving-beam/control ledger. No issue24 tensor result changed.


## 2026-10-03 — gate hosted verification

The regular hosted workflow also passed all190 tests. Saved research code and public record were read back successfully. These are conventional software experiments, not physical replication or flight. The private research PR remains open.


### 2026-10-03 — environmental heat exchange

Added a stationary conventional-physics cooling calculation that separates emitted radiation, absorbed environmental radiation and deposited heater energy. Synthetic cases show equilibrium can have nonzero opposing radiation channels despite zero net cooling. All 199 tests pass locally, including exact-solution and integration-refinement anchors. Five bounded independent worker reviews found no defect. Physical calibration, material properties, background geometry, other heat paths and radiation momentum coupling remain unresolved. Next gate is separately accounted single-pass optical absorption, keeping laser absorptance distinct from cooling emissivity. No new patent claim, hardware, thrust, flight or FTL result. Reference constant: https://physics.nist.gov/cgi-bin/cuu/Value?sigma . Detailed implementation remains private in open PR #29; hosted validation pending.


Hosted verification: regular workflow https://github.com/mommommy1960-lang/flux-drive-kernel/actions/runs/37137989566 passed for implementation 2332b10623c4080d9ca0b7a2db7b7c65b89e0c6f. Job 111246348538 confirms 199 tests. Subsequent verification edits are documentation only.



### 2026-10-03 — optical deposition, sensitivity and three patent leads
Integrated a stationary single-pass optical energy budget with environmental cooling. Only absorbed power heats the model; missed, reflected and transmitted light remain explicit. Laser absorptance is separate from thermal emissivity. Eleven new tests bring the local suite to210 passing tests; five bounded workers contributed source/physics/numerical reviews. Executed a further finite synthetic sensitivity grid; it is not material calibration, a global safety bound or a measured result. No momentum/recoil/cavity-control result.

New inventor credit and screening outcomes:
- M’dimoir Quaw, GB2562139A: https://patents.google.com/patent/GB2562139A/en . Published2018-11-07. Warp/virtual-particle claims not adopted as a source. Displayed Pending conflicts with withdrawal/refusal and a later reinstatement request; current official status is unresolved.
- John Baker,Leland F.Collins,Thomas C.Kuklo,James V.Micali, US5156459A: https://patents.google.com/patent/US5156459 . Granted1992-10-20. Retain coolant-flow/temperature calorimetry as a calibration reference; displayed fee-related expiration is not a legal clearance.
- Donald L.Decker,Paul A.Temple, US4185497A: republished issued text https://patents.justia.com/patent/4185497 . Granted1980-01-29. Electrical-substitution calibration/stray-light controls are candidate measurement leads; primary-host and family/status verification incomplete, not a cleared dead patent.

Primary reference credit: NIST IRIS https://www.nist.gov/laboratories/tools-instruments/infrared-reference-integrating-sphere-iris and NASA thermal control https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/ . Actual contribution is offline conventional-physics implementation and source screening. No hardware, flight, FTL or freedom-to-operate claim. Private detail preserved in open PR29 and issue25; issue24 unchanged. Next measured gate is traceable absorbed-heat/optical-power calibration and material/background inputs with uncertainty. Next software gate is time-resolved deposition; momentum and cavity loading remain unresolved.


Hosted verification follow-up,2026-10-03: current210-test implementation has failed GitHub runs with no recorded test steps; logs unavailable, cause unverified. Local210-test pass remains valid, but no hosted pass is claimed. https://github.com/mommommy1960-lang/flux-drive-kernel/actions/runs/37139587196 . Runner/failure-detail verification is an open gate; offline research can continue.


## 2026-10-03 — time-resolved thermal ledger and two calibration/control references

**Completed work:** a conventional piecewise optical-heating calculation now preserves optical input, radiative exchange, stored heat and elapsed-time channels across changing input intervals. Thirteen focused tests plus the existing suite passed locally, for 223 local tests total. Equal deposited optical energy produced different final temperatures when its timing changed, because earlier heating had more time to radiate. This is a synthetic lumped-body calculation, not measured hardware performance.

**Numerical evidence:** a zero-background cooling case converged toward the independent exact gray-body solution under step refinement. Optical and thermal ledgers close separately and together. Internal reviewers checked the physical bookkeeping, state continuity, numerical bounds and limitations; this is not external peer review or physical replication.

**Preserved corrections:** two development attempts failed before evaluating physics—one test-harness method-name collision and one syntax error. Both are retained in the private record and were corrected before the passing run.

**Hosted verification blocker:** the latest GitHub Actions jobs did not begin any test step. GitHub identifies failed account payments or an insufficient Actions spending limit. Hosted verification therefore remains blocked; the 223-test result is local evidence only.

**Credited prior art:** Ephraim Secemski's [US5316380A](https://patents.google.com/patent/US5316380A/en) supplies a calorimetric optical-versus-electrical calibration concept. Stephen P. Sandford and Charles W. Antill, Jr.'s [US6175579B1](https://patents.google.com/patent/US6175579B1/en) supplies a cavity-lock/control architecture that exposes control-power channels which must be counted. The project has not adopted either as propulsion. Displayed expiration/lapse metadata is not a legal conclusion or a freedom-to-operate finding.

**Next gate:** calibrate the time-resolved heat model using traceable optical and electrical pulses with wavelength-dependent optical fractions and temperature-dependent thermal properties. Separately, couple emitted-energy intervals to the existing momentum ledger and account for every cavity-control energy channel. No anomalous force, warp field, flight or faster-than-light result is established.


## 2026-10-03 — bounded thermal-radiation momentum comparison

Completed a synthetic zero-background cooling/momentum comparison. Radiation isotropic in the body's rest frame carries momentum in a moving observer's frame, while cooling reduces the body's invariant mass without accelerating it. This is a conventional no-acceleration result, not thrust or flight evidence.

Seven additional checks cover analytic cooling, frame transformation, energy bookkeeping, duration and numerical rejection boundaries. All230 tests pass locally; no new hosted pass or independent review is claimed. Hosted verification remains blocked by the previously diagnosed GitHub account restriction.

Project contribution: coupled its existing thermal and radiation-accounting models within a deliberately restricted domain. Earlier source credit remains intact; no new patent discovery or hardware measurement occurred. Thermal properties and angular response remain assumed rather than measured. The next gate is conserving incoming as well as outgoing energy and momentum before expanding to heating, background radiation or directed emission. No working Flux engine or FTL result is established.


## 2026-10-03 — incoming radiation and balanced-cycle reference

Implemented and tested a bounded conventional incoming-radiation accounting helper. Directed absorbed radiation supplies both internal energy and motion; isotropic rest-frame input increases internal energy without changing velocity. A matched isotropic input/output cycle restores the original state, providing a negative reference against false net gains.

Seven new analytic/regression checks pass; all237 tests pass locally. This is this project's standard relativistic accounting implementation, not measured performance, a new patent invention, independent review, or a full environmental/thermal simulation. No hosted pass claimed; the known account restriction remains unresolved.

Detailed parameters and implementation stay in the private record. The next interface gate is preserving precision and global source/export energy/momentum across incoming and outgoing event sequences. Measured emission/material data and control costs remain missing physical inputs. No anomalous propulsion, flight or FTL result established.


## 2026-10-03 — cavity loss versus absorbed heat

Screened [US6233052B1](https://patents.google.com/patent/US6233052B1/en), credited to Zare, Harb, Paldus and Spence, as a cavity-decay measurement reference. Its displayed expired status does not establish freedom to operate; related rights need official review.

Added a conventional synthetic loss-budget gate with five tests. All242 tests pass locally. Key negative result: the same total light-decay history can have different absorbed heat; independent loss-channel measurements are necessary. No patent mechanism is adopted as propulsion. Detailed source review, assumptions and numerical limits remain private.

Next inference gate is sensitivity to detector offset, noise and multiple decay modes. Hosted verification remains billing-blocked. No physical engine, flight or FTL result established.


## 2026-10-03 — New source screen: observer-independent warp verification

Primary source: An T. Le, *Observer-robust energy condition verification for warp drive spacetimes*, arXiv:2602.18023v6, revised 2026-09-24, https://arxiv.org/html/2602.18023v6 . Source review, not an independently reproduced result. The paper proposes S-lemma 4x4 matrix tests and interval bounds for energy conditions without a rapidity cutoff. Its four reference geometries show NEC violations at the reported parameters; this is not a universal impossibility theorem and not a result for Flux. The hollow/smoothed Fuchs shell is outside its matched four-drive benchmark.

Contribution: candidate verification method, not a physical warp source. Existing Flux observer sampling must not be advertised as an all-observer certificate. Before adoption, reproduce the matrix criterion against analytic Type-I pass/fail cases, construct explicit violating null/timelike witnesses, and compare with the existing sampled evaluator under the same tetrad and sign conventions. A finite sample finding no violation remains inconclusive. No engine component or energy-condition clearance adopted in this screen. The previously logged Cole negative-frame-dragging patent and Celmaster/Rubin Lentz critique were not duplicated. No legal freedom-to-operate conclusion. Issue #24 unchanged: no new Flux tensor calculation completed.


Follow-up synthetic diagnostic: the existing finite observer sampler returned positive sampled margins for a deliberately constructed tensor with a known violating observer. This is a verification limitation, not a result for Flux or measured hardware. An all-observer certificate requires a stronger independent test.


## 2026-10-03 — Verification evidence safeguard

A numerical evidence-labeling safeguard now distinguishes a sampled violation from an inconclusive positive scan. Two synthetic regression tests preserve the previously demonstrated sampling limitation. All 244 local tests passed; hosted validation is not claimed. Motivation credited to An T. Le, https://arxiv.org/abs/2602.18023v6 . This is a project software safeguard, not an independent replication of the paper, a physical warp mechanism, or flight evidence. Stronger all-observer certification remains unresolved.


## 2026-10-03 — Physical source screening: Casimir vacuum

Reviewed the ideal parallel-plate vacuum stress tensor and executed a conventional scale calculation, credited to Gorban, Julius and Cleaver and their Brown/Maclay source, https://arxiv.org/html/2312.00898v1 . A negative vacuum contribution is not enough to source the proposed transport geometry: pressures, material boundaries, positive plate mass, supporting stresses and conservation must all be included. This project has not matched the full apparatus tensor to Flux or measured an apparatus. Garattini/Tzikas https://arxiv.org/abs/2507.19134 is an additional near-throat theoretical lead, not reproduced or adopted. No physical warp mechanism established. Material response and complete source accounting are unresolved gates.


## 2026-10-03 — Casimir candidate: narrow source mismatch found

Executed a tensor comparison against one existing frozen wormhole model. The ideal parallel-plate vacuum contribution has incompatible invariant stress-energy trace, so it alone cannot source that specific geometry. This does not reject all quantum sources, alternative geometries, or a complete apparatus including matter and supports. Added a negative regression; 245 local tests pass, hosted pass not claimed. Source credit: Gorban, Julius, Cleaver (and Brown/Maclay), https://arxiv.org/html/2312.00898v1 . No physical measurement, warp field or flight established. Complete apparatus source remains unresolved.


## 2026-10-03 — Combined-source gate and research variants

A new analytic residual test excludes one ideal aligned Casimir contribution plus any dominant-energy-condition-satisfying residual for the existing frozen wormhole model. This is narrow, not an exclusion of every material, quantum state, or geometry. Regression preserved; 246 local tests passed. New literature screening credited to Barcelo/Visser https://arxiv.org/abs/gr-qc/0003025 and Bronnikov https://arxiv.org/abs/2206.09227 . Their theoretical scalar-field constructions are not demonstrated apparatuses or independently reproduced by this project. Founder authorized geometry/mechanics research variants; original baseline and failures must remain intact. No flight or warp source established.


## 2026-10-03 — Local geometry variant, conservation gate

A throat-only algebraic variant can match the ideal Casimir energy/pressure proportions when the shape and gravitational time-rate profile are adjusted. A fixed-gap ideal contribution then fails the local conservation equation. A varying source amplitude is a formal local condition only; it is not a validated real apparatus or complete spacetime. 247 local tests pass. Full geometry, material/source accounting, stability and independent verification remain unresolved. Credit standard Morris-Thorne equations (Lemos/Lobo/Oliveira https://doi.org/10.1103/PhysRevD.68.064004) and Casimir tensor Gorban/Julius/Cleaver https://arxiv.org/html/2312.00898v1 , Brown/Maclay. No hardware measurement or warp/flight established.


## 2026-10-03 — Formal source continuation, boundary failure preserved

Extended the previous throat-only matching calculation into a formal static tensor model. It satisfies the tested energy/pressure components and local conservation away from the throat, but fails the ordinary asymptotically flat outer-boundary condition and is not a localized source. This prescribed tensor is not a verified Casimir apparatus. A corrected scratch algebra error is retained in the private record. 248 local tests pass; independent tensor validation, boundary matching, physical source and stability unresolved. Source credit Lemos/Lobo/Oliveira https://doi.org/10.1103/PhysRevD.68.064004 and Gorban/Julius/Cleaver https://arxiv.org/html/2312.00898v1 , Brown/Maclay. No novelty or hardware claim.
