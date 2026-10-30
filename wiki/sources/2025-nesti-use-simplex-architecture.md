---
type: source
id: 2025-nesti-use-simplex-architecture
status: reviewed
read: full
kind: test
sources: [2025-nesti-use-simplex-architecture]
updated: 2026-10-29
---

# Nesti et al. 2025: The Use of the Simplex Architecture to Enhance Safety in Deep-Learning-Powered Autonomous Systems

Federico Nesti, Niko Salamini, Mauro Marinoni, Giorgiomaria Cicero, Gabriele Serra, Alessandro Biondi and Giorgio Buttazzo (Scuola Superiore Sant'Anna, Pisa; Accelerat). Preprint, September 2025. [arXiv](https://arxiv.org/abs/2509.21014).

## What it shows

- **An architecture.** The authors run two domains on one board, isolated by the type-1 real-time hypervisor CLARE: a *rich* domain with Linux running the neural network, deemed untrustworthy in safety, security and timing, and a *safe* domain running sensing, actuation, a safe controller and a safety monitor. The monitor switches to the safe controller when it judges the state or the network untrustworthy, and back when it is safe again (§3). The AI component is "untrustworthy by definition" (§2).
- **Simplex in three parts.** A simple safe controller, a high-performance controller without guarantees, and a safety monitor whose switching rule "is tailored for the specific system and requires to be designed for each use case" (§2.2). The paper traces Simplex to Sha, Rajkumar and Gagliardi 1994, for safely testing new controllers, and to Seto et al. 1998, for safe online upgrades (§2.2, refs. 14 and 32).
- **Pendulum.** On a Zynq UltraScale+ (ZCU102), a neural controller balances a Furuta pendulum; the safe domain runs the Erika3 RTOS with a 4 ms control period. The monitor switches when the state leaves an ellipsoid estimate of the safe controller's region of attraction, and back when it is well inside it. A push sends the system to the safe controller, which recovers (§4.2, §4.3). The rich domain has no direct access to any device in the control loop (§4.1).
- **Timing on the pendulum.** The round trip from the safe domain through the neural network and back took at most 3,976 µs over 10,000 samples, against the 4 ms period (Table 2). The monitor also checks that the network's output is fresh, so a late answer counts as a fault (§4.1).
- **Rover.** On a Kria KR260, a rover navigates a corridor with a LiDAR and a camera. The safe domain owns the LiDAR, preprocesses it and passes the distances to the rich domain; the camera is processed only on the rich side. The safe side enforces three distance zones with speed limits and a stop that a person must acknowledge. The authors keep the camera out of the safe path because images are unreliable and certified LiDAR exists (§5.2). With the network's output doubled to simulate an attack, the zones limited speed and the rover finished without collision; a box thrown in front of it triggered a stop within the 100 ms LiDAR period (§5.3, §5.4).

## How

Two physical systems, each with a hand-built safety monitor and safe controller and a neural controller trained in simulation. Evidence is a set of runs on the real systems, timing histograms and the absence of collisions or falls in these runs (§4.3, §5.4).

## Limits

The authors state:

- A wrong command could move the pendulum outside the true region of attraction within one step; a one-step prediction would guard against it but was left out for time and resource reasons, since it "never occurred during our extensive experiments" (§4.2).
- The ellipsoid is checked for false positives only by sampling, which "cannot provide an absolute guarantee" (§4.2).
- The lateral safety zones on the rover were kept small on purpose to avoid false stops, and rely on the network's output staying between −1 and 1 m/s because of its tanh activation (§5.4).
- The architecture adds complexity in hardware and software, and partitioning devices between domains complicated the rover's design and debugging; ROS 2 brought "unexpected behavior" (§6).

A careful reader adds:

- **The safe domain on the rover is Linux.** Both VMs run Ubuntu with ROS 2; the safe one is stripped down. The safe path there is isolated, not small or analysed.
- **Little margin on the pendulum.** The worst observed round trip is within 25 µs of the 4 ms period; it is an observation over 10,000 samples, not a bound.
- **Tests, no proof.** The safety argument rests on runs and on the hypervisor's isolation; the paper does not claim the hypervisor is verified.

## Against the wiki

- [[2018-klein-formally-verified-software]]: the authors cite seL4 in UAVs as related work; this paper uses a different hypervisor.
- [[simplex]]: created with this source.

## For zOS

- [[safety-path]]: the zOS paper maps Simplex onto its layers in Section 4 and dates the pattern to 2001 (Sha 2001; also Table 1 and the Epilogue). This source dates its origin to 1994 and 1998. Our reading: the date in the paper rests on a source the wiki cannot read and is earlier in the literature than the paper says.
- Two lessons fit zOS. The switching rule has to be designed per system, as the paper's "for one robot and one task" says. And the safe side owns the sensors it relies on and leaves out inputs it cannot trust, here the camera.
- Our reading: the rover's stop that a person must acknowledge is the pattern the paper's "a controller that stops at every doubt is safe and useless" warns about, and the zones are the answer: degrade speed before stopping. The zones also show a hidden dependency: the lateral margin relied on a bound in the learned network's output layer.
