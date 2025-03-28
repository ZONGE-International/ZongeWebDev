# UAV (Drone) Magnetic Survey (nT)

## Method

### Introduction

Total magnetic intensity varies laterally in proportion to the amount of magnetic minerals present. It can be useful to find both magnetic highs and magnetic lows depending on the application and target type.  
Measurements are made along lines using a total-field magnetometer suspended from an Unmanned Aerial Vehicle (Drone). It is necessary to perform calibration flights for compensation and perform diurnal corrections on the dataset using a magnetic base station. All pilots are FAA part 107 certified and operations are carried out in compliance with Zonge’s UAV SMS program.
Drone magnetics strikes a balance between helicopter borne surveys and ground surveys. There may be a bit less detail than ground surveys but the draping using an RTK based drone is generally better and so there can be more detail than helicopter surveys. Helicopter surveys are generally the most cost-efficient option for large areas.

{{< figure src="/img/mag_anomalies.jpg" title="" width=800 >}}

---

## Applications

- Mapping mafic and ultramafic igneous rock types. Generally felsic rocks are not strongly magnetic. Many rocks are weakly magnetic which can still be detectable.
- Detecting magnetite destructive alteration in porphyry and epithermal systems (including geothermal).
- Mapping structure if there is variation in TMI between the hanging and footwall, or if there is observable offset in the mapped features.
- Mapping steel casing in abandoned wells and other magnetic anthropogenic features.

---

## Survey Design

| **Parameter**    | **Description**                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Depth**        | DOI is based on the size of the magnetic body, its intensity, and sources of noise. It is generally safe to assume features that have anomalous TMI can be seen at depth if they are sufficiently large; certainly, if they are as laterally expansive as they are deep. Without doing an inversion depth is based on interpretation of wavelength and gradient of anomalous feature. |
| **Line-Spacing** | Typically, 25m-100m depending on the level of detail required. 25m line-spacing is generally only practical in areas where it is possible to fly low.                                                                                                                                                                                                                                 |
| **Scale**        | Anywhere from 100’s to 1,000’s of line-km is practical. At a certain point if the additional resolution of the drone survey is not required then it may make more sense to use a helicopter.                                                                                                                                                                                          |
| **Production**   | 50-120 line-km/day                                                                                                                                                                                                                                                                                                                                                                    |
| **Processing**   | Data are processed and gridded using Oasis Montaj. The MAGMAP module is used for filtering including the RTP and 1VD.                                                                                                                                                                                                                                                                 |

---

## Instrumentation

- Geometrics MagArrow, GEM DRONEmag, testing other magnetometers

- DJI M300, working on switching to open-source ArduPilot based drone

- GEM GSM-19 Overhauser magnetometer for base station

---

## Deliverables

- Contoured plans of TMI reduced to pole.

- Contoured plans of First Vertical Derivative of the TMI reduced to pole.

- Magnetic inversions can be completed upon request.

---

## Survey Life Cycle

1. Planning, permitting, and FAA flight compliance
2. UAV and magnetometer setup and calibration
3. Flight execution with QA/QC
4. Diurnal correction and data processing
5. Advanced filtering and derivative products
6. Final map generation and optional modeling

{{< figure src="/img/survey_life_cycle.jpg" title="" width=800 >}}

---

## Case Studies and Resources

- [Zonge UAV Mag Projects]
- [Examples from ultramafic terrain mapping]
- [Internal case study resources and white papers]
