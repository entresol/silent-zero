---
type: source
id: 2026-jager-context-dependent-runtime
status: reviewed
read: full
kind: test
sources: [2026-jager-context-dependent-runtime]
updated: 2026-11-21
---

# Jäger et al. 2026: context-dependent regions of attraction for a multi-candidate Simplex

Georg Jäger, Nils-Jonathan Friedrich, Norman Seyffer (TU Bergakademie Freiberg), José Cecílio and António Casimiro (LASIGE, University of Lisbon). "Context-dependent Runtime Construction of Safe Regions of Attraction from Design-Time Identification for Multi-Candidate Simplex Architectures", arXiv 2610.35040v2 [cs.RO], 27 October 2026. A preprint. [arXiv](https://arxiv.org/abs/2610.35040). Read: the full text; the reference list was read only for the works the text names.

## What it shows

- **The problem.** A [[simplex]] switch is only as permissive as the certified region of attraction (RoA) of its safe controller, the set of states from which that controller is guaranteed to recover the system. A tight region means premature switching and lost performance. The authors review safety filters, blending and runtime reachability and judge them against Simplex on guarantee strength, conservatism, compute cost and certification effort. That comparison is a literature review, not a measurement (§II).
- **Design time.** A two-stage procedure certifies a safe controller. Stage 1 finds a contraction ellipsoid by interval verification; stage 2 runs Taylor-model reachability, with the state and parameter space split into cells and bins, to collect the states that provably stay safe and enter the ellipsoid. The result, the "recovery profile", holds the ellipsoid, the safe regions per parameter bin and a maximal dwell time (§III-B, Algorithms 1, 2).
- **Runtime.** From the recovery profile the decision module builds a context-dependent safe region as the intersection of the regions of the bins the current context can touch. Fewer bins give a region at least as large as the global intersection (§III-B3, Eq. 7). Several safe candidates are held at once. A proposed action passes if one candidate can recover from the predicted next state, and control returns to the learned side once the state is inside the candidate's ellipsoid, with a hysteresis ratio (§III-C, Algorithms 3 to 7).
- **Setting.** Path tracking for a differential-drive robot with the safety requirement |lateral error| ≤ 1 m (§IV-A). The safe candidates are Regulated Pure Pursuit controllers with two certified configurations, γ4 (1.0 m/s; 752 safe cells) and γ15 (1.5 m/s; 664 cells), chosen from 24 configurations (§IV-B, Table I). Certifying one configuration took about 100 min 37 s on a laptop with a Core Ultra 7 155H and 64 GB (§IV-B).
- **ODE simulation.** Four Monte-Carlo campaigns of 1,000 runs each, with a fault from 2 s to 5 s that inverts the angular velocity of the uncertified high-performance controller, which is the same Regulated Pure Pursuit controller as the safe one (§IV-C). The maximum lateral deviation stayed between 0.964 and 0.982 m in all four, within the 1.0 m requirement. The authors conclude that a one-step prediction suffices when the model dynamics are matched. Switching from γ4 to γ15 gave a mean switching deviation of 0.439 m against 0.406 m (γ4 alone) and 0.392 m (γ15 alone), and a mean recovery time of 2.463 s between the two single candidates' 2.819 s and 2.337 s (§IV-C, Table II).
- **Unmodelled dynamics.** In Gazebo, with wheel slip and sensor noise, a one-step horizon was not enough. Both candidates violated the requirement for prediction horizons up to 5 control periods; horizons of 10 and 15 held it in the circular case, and the authors set 10 (Table III, §IV-D). The hysteresis ratio had no systematic effect there (§IV-D). With switching on a synthetic cosine path at horizon 10, the maximum deviation over 10 runs was 0.894 m (§IV-D).
- **Hardware, circular tracks.** On the robot, with 5 to 10 injected faults per setting, horizon 1 violated the requirement for all configurations; horizon 10 did so for the γ4 + γ15 switch at curvatures 0.2 and 0.9; horizon 15 kept the maximum deviation below 0.69 m throughout (§IV-E1, Table IV). The authors say only h = 15 kept safety in all configurations. The text states that the simulation closely approximates the real behaviour while physical deployment still needs conservative margins (§IV-E1).
- **Overhead.** Over 81,749 decision cycles in the circular experiments, the decision module took 0.0281 ms on average (standard deviation 0.0396 ms) and 4.1303 ms in the worst case, against a 50 ms control period: under 0.1 per cent on average, under 10 per cent at worst (§IV-E1). The abstract states "0.028 ms average, 4.13 ms worst-case, under 10 %".
- **Learned controller.** A neural network trained by behavioural cloning for 50 epochs on the authors' own manually driven data was shielded with horizon 12 on an urban track. In three runs the maximum deviation was 0.37 to 0.41 m, the longest intervention 1.05 s and the activation count NHA given as 3, which the authors read as an enlarged operating envelope (§IV-E2, Table V).

## How

A Simplex controller with an uncertified high-performance side (a learned network only in §IV-E2) and a set of certified safe controllers, in three stages: ODE simulation of the same error model used for certification, a ROS 2 and Gazebo simulation, and a custom differential-drive robot with an Intel Core i7-12700TE (35 W) (§IV-A). The context is the local path curvature, estimated by fitting a circle to a sliding window of waypoints, with window size 5 in the ODE runs and 30 elsewhere (§IV-B2). The offline reachability uses TMJets (cited as JuliaReach, [39]) (§IV-B3); at runtime the decision module needs only set intersections and membership checks (§III-B3).

## Limits

The authors state the following.

- The simplified dynamics used to certify the regions miss real effects. The prediction horizon on hardware is tuned by experiment; incorporating slip, actuator latency and acceleration bounds in the offline pipeline might replace it with certified bounds (§IV-D, §V).
- The latency analysis is preliminary. The gap between average and worst-case execution time needs a formal timing and schedulability analysis (§IV-E1, §V).
- The runtime region is bound to the parameter space fixed at design time, and needs contextual knowledge of the active parameters, here the curvature estimate (§III-B3). The window size trades false negatives against false positives (§IV-B2).
- Whether the Lyapunov hysteresis is needed, and whether the method carries to other system classes and higher-dimensional state spaces, remain open (§V).

A careful reader adds the following.

- The result is for a two-dimensional error state of a ground robot. Nothing is shown for an arm or a learned policy that acts on images or language. Path tracking is the only task.
- The safety proof covers the model with continuous control. The deployed claim rests on a horizon chosen from experiments, so the guarantee on hardware is empirical, with 1 to 28 safe-controller activations per setting in Table IV.
- The behavioural-cloning test is three runs of one configuration with no unshielded control and no switch-off comparison, so the statement that the envelope was enlarged is not measured against the narrower single-candidate case on hardware. The claim for it rests on the ODE campaigns.
- The decision module's timing is a measurement, over all circular real-world experiments, on a 35 W processor and not on a microcontroller; the worst case is about 147 times the mean, and the text gives no figure for scheduling or interference. Whether the 4.13 ms includes the curvature fit is not stated.
- The curvature estimate comes from waypoints whose source and trust the paper does not discuss; a wrong estimate could shrink or enlarge the context region. Our reading is that a safety loop of this kind needs its own account of such inputs.
- The comparison with safety filters and blending is argued from the literature. No filter was run on the same task.
- The paper is a preprint.

## Against the wiki

- [[simplex]]: **extends**. It is a Simplex whose switching rule is built from design-time artifacts, with several safe controllers and a switch between them; the wiki so far has a per-system rule and a variant that lets information flow both ways ([[2026-bansal-synergistic-simplex-cooperative]]). It bears on the open question there. A one-step prediction guarded safety with matched dynamics in simulation (§IV-C), yet on hardware only a horizon of about 15 control periods kept it in every configuration (§IV-E1). That reaches further than the one-step prediction [[2025-nesti-use-simplex-architecture]] names and leaves out (§4.2). The paper cites Nesti et al. among static-ellipsoid approaches it calls conservative for nonlinear systems.
- [[safety-path]]: **extends**, with a second kind of evidence next to Nesti et al.: a switching rule derived by reachability and contraction from a model, with an uncertified high-performance controller on the other side. It still proves safety only for the model; our reading: it does not give the proof the wiki page found missing for a whole safe controller on real hardware.
- [[real-time-loops]]: **extends** with one timing figure, a decision cycle of 0.0281 ms mean and 4.13 ms worst case against 50 ms, measured, with no bound; compare the 3,976 µs worst round trip of the isolated domain in Nesti et al. Its own authors name a timing analysis as future work (§V); see [[wcet-analysis]].
- [[mixed-criticality]]: no direct link; the paper does not discuss isolation of the two sides.

## For zOS

[[safety-path]]: no change of state. The source is evidence that the switch of a Simplex can be cheap in compute and that candidate safe controllers can be certified offline for a stated model. It also shows the cost, certification time per controller, and a horizon that must be tuned on the real plant. [[real-time-loops]]: no change of state; a timing reference only. Nothing in zOS is built.
