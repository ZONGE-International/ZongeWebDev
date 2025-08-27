+++
title = "Software"
banner = "img/person_w_vista.jpg"
weight = 1
+++

# Zonge Software Programs

<style>
/* ===== Zonge-style software table ===== */
.zg-softwrap {
  --zg-border:#e2e8f0;      /* light gray */
  --zg-head:#f7fafc;        /* header bg */
  --zg-zebra:#fbfdff;       /* zebra rows */
  --zg-text:#1a202c;        /* dark text */
  --zg-muted:#4a5568;       /* muted text */
  font-family: system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif;
  color: var(--zg-text);
  margin: 1.5rem 0;
}
.zg-softwrap h2{
  margin:0 0 .5rem 0;
  font-size: clamp(1.25rem, 2vw, 1.6rem);
}
.zg-note{font-size:.92rem;color:var(--zg-muted);margin:.25rem 0 1rem}

.zg-table{
  width:100%;
  border-collapse: collapse;
  border: 1px solid var(--zg-border);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 1px 0 rgba(0,0,0,.03);
}
.zg-table th, .zg-table td{
  padding: .75rem 1rem;
  vertical-align: top;
  border-bottom:1px solid var(--zg-border);
}
.zg-table th{
  background: var(--zg-head);
  text-align:left;
  font-weight: 600;
  letter-spacing:.02em;
}
.zg-table td:first-child{
  white-space:nowrap;
  font-variant-numeric: tabular-nums;
  font-weight:600;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
.zg-table tr:nth-child(even) td{
  background: var(--zg-zebra);
}
.zg-table tr:hover td{
  background: #f1f5f9;
}
@media (max-width: 720px){
  .zg-table thead{display:none;}
  .zg-table, .zg-table tbody, .zg-row, .zg-table tr, .zg-table td{display:block;width:100%}
  .zg-table tr{border-bottom:1px solid var(--zg-border)}
  .zg-table td{
    border:none;
    padding:.55rem .9rem;
  }
  .zg-table td:first-child{
    padding-top:.8rem;
    font-size:1rem;
  }
  .zg-table td[data-label]::before{
    content: attr(data-label) " ";
    display:block;
    font-size:.8rem;
    color:var(--zg-muted);
    margin-bottom:.15rem;
    font-weight:600;
    letter-spacing:.02em;
    text-transform:uppercase;
  }
}
</style>

<div class="zg-softwrap">
  <h2>Zonge Software Programs</h2>
  <div class="zg-note">Each program has a one-line description. Add/remove rows as needed.</div>

  <table class="zg-table">
    <thead>
      <tr>
        <th>Program</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <!-- ===== Your rows (duplicate/modify) ===== -->
      <tr>
        <td>CSAVGW</td>
        <td data-label="Description">Averages and performs QC on CSAMT/NSAMT electromagnetic data.</td>
      </tr>
      <tr>
        <td>TEMAVGW</td>
        <td data-label="Description">Averages and QC’s transient electromagnetic (TEM) field data from .raw, .dnt, .cac, and .zdb formats.</td>
      </tr>
      <tr>
        <td>CRAVGW</td>
        <td data-label="Description">Processes complex resistivity (CR) data; compatible with GDP-3224 and ZEN receivers.</td>
      </tr>
      <tr>
        <td>CSINV</td>
        <td data-label="Description">Inversion software for CSAMT/NSAMT resistivity modeling.</td>
      </tr>
      <tr>
        <td>CSPLOT</td>
        <td data-label="Description">Contour/section plotting tool for CSAMT/MT model outputs.</td>
      </tr>
      <tr>
        <td>MTEDIT</td>
        <td data-label="Description">Reviewing and averaging magnetotelluric impedance data.</td>
      </tr>
      <tr>
        <td>CSV2OUT</td>
        <td data-label="Description">Utility for converting CSV data to standard output formats.</td>
      </tr>
      <tr>
        <td>TEM Modeling Software</td>
        <td data-label="Description">Smooth-model TEM inversion to generate resistivity-vs-depth profiles.</td>
      </tr>
      <tr>
        <td>Modeling AMT/CSAMT</td>
        <td data-label="Description">Generates resistivity sections from AMT/CSAMT field data.</td>
      </tr>
      <tr>
        <td>Utilities: Color Contour &amp; Cole–Cole</td>
        <td data-label="Description">Plotting utilities and Cole–Cole fitting for IP/CR data.</td>
      </tr>

      <!-- ===== Example placeholders for more items you may add =====
      <tr><td>CCINV</td><td data-label="Description">Cole–Cole inversion for time/frequency-domain IP data.</td></tr>
      <tr><td>S2DPLOT</td><td data-label="Description">Simple 2-D plotting of sections and plan-views from model grids.</td></tr>
      <tr><td>MODSECT</td><td data-label="Description">Section builder/visualizer for model layers and constraints.</td></tr>
      <tr><td>TEMTRIM</td><td data-label="Description">Skips noisy decay gates and trims outliers in TEM stacks.</td></tr>
      -->
    </tbody>
  </table>
</div>
