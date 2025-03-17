# Time-Domain Electromagnetics

The TDEM (or TEM, they are equivalent) method is one of the easiest electromagnetic methods to initially understand, but is one of the more difficult to master.

## Theory

The figure below outlines the basic signals observed by a TDEM system. The first panel is the current waveform, with a fairly slow turn-on, a constant current on-time, followed by a fast - linear - turn-off. This current, generally driven through a loop of wire on the earth's surface, creates a secondary EMF in the subsurface proportional to the derivative of source (panel 2). This EMF then generates secondary current in the earth, which then drives a secondary magnetic field related to the electrical properties of the subsurface. It is this magnetic field, measured during the off-time, that is the basis of the method.

{{< figure src="/img/methods/temwaveform.png" title="TDEM Waveforms" width=500 >}}

## Strengths and Weaknesses

The TDEM system is an effective tool for the mapping of conductive features in the subsurface. If measuring only the vertical magnetic field, the primary signal couples primarily to the horizontal structure, making the TDEM method effective in the mapping of alluvial aquifers and other lpw-angle structures. If the horizontal fields are measured, deeping conductive structures can also be effectively imaged - this is particularly true if the background resistivity is high. It is the successful mapping of conductive features, from fluid filled sediments to massive sulfides and metallic objects, that has led to the widespread use of TDEM tools.

There are two primary limitations to the method. The first is the depth of investigation. Figure 3 below illustrates the relationship between decay time and depth, with signals related to deeper changes in electrical resistivity apprearing later in time and therefore smaller given the exponential decay. But while waiting until later in time will increase the depth of investigation, at some point the signal is so small that it is no longer detectable above the combined instrument and cultural noise. The solution to the issue is to increase the moment of the transmitter. But this solution points at the second difficulty in application

### Depth of investigation:

The depth of exploration attained can vary from 10s of meters to over 1000 meters, depending upon transmitter loop size, available power from the transmitter, and ambient noise levels.

### Lateral Resolution:

### Straightforward Logistics:

TEM equipment consists of a transmitter and receiver, which may be in separate enclosure boxes with an external power source for the transmitter or contained in a single box.
Field logistics vary depending upon the target, but all configurations are nonintrusive and low-impact. For large scale (deep sounding) TEM surveys a typical field crew consists of three or four people, with one pick-up truck at the transmitter site and one at the receiver site. At the receiver site, the equipment can be carried by backpack, and no off-road
driving is needed. Shallow surveys using a fast-turn-off system require one to three people and all of the equipment is backpack portable. Depending upon the target, the set-up of
the equipment system varies greatly from large loops on the ground, to cartmounted systems or boat-towed arrays. When not self-contained in a cart-mount or towed system, the transmitter consists of a thin, insulated surface wire laid out along the ground. Vehicle access along the length of the transmitter is not needed.

### Integration with other methods:

### Susceptibility to Cultural Noise

# Logistics

A transmitter, typically a loop of wire laid on the ground, is driven by a timevarying current. The change in current and the resulting EM field establish an image current within the earth equal in magnitude, but opposite in polarity, to that of the transmitter. This image current then interacts with conductive materials in the earth below creating secondary magnetic fields that are measured at the receiver site.

## Receiver

## Source

# Targets

## Examples

### Groundwater

TDEM is a common tool for the mapping of groundwater systems in alluvial enviroments, as the surface transmitter loop couples well into the layered enviroment. Zonge and its customers have used this for numerous investigations of the electrical resistivity using both static and towed arrays.

Mike Hatch at University of South Australia mapped a large section of the River Murray with a Zonge Nanotem system.

[**TEM survey on the River Murray to map salt intrusion**](/documents/rivertem.pdf)

Fitzpatrick et al. at CSIRO compared the resistivity values obtained using the river-borne system with several airborne systems. The result:  
-The observed resistivities from all the methods compared very well with each other.
-The river borne TEM was financially competitive with airborne survyes on a per kilometer basis.

[**Comparison of Airborne and Groundbased TEM Systems on the River Murray**](/documents/temcomparison.pdf)

### Massive Sulfides

TDEM is a very effective tool for the detection of massive sulfide mineral deposits, particularly in areas of high background resistivity.

# References

Nabighian, M.N., “Quasi-static transient response of a conducting half-space — an
approximate representation.” Geophysics, 44, pp. 1700-1705.

# Required Instruments

[GDP Receiver](/gdp3224/)

[NT-20 Transmitter]({{< ref "nt20" >}} 'Fast Turn-off TEM Transmitter')

[Transmitter](/zt30b/)

[GGT-10 Transmitter]({{< ref "ggt10" >}} 'Medium Power Transmitter')

[GGT-30 Transmitter]({{< ref "ggt30" >}} 'High Power Transmitter')

[XMT-G Transmitter Controller]({{< ref "xmtg" >}} 'Transmitter Controller')

[ZMG-9 Generator]({{< ref "ggt10" >}} 'Medium Power Generator')

[ZMG-30 Generator]({{< ref "ggt30" >}} 'High Power Generator')

[TEM-4 Antenna]({{< ref "tem4" >}} 'db/dt Magnetic Field Sensor')
