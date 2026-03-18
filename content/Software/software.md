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
  <p class="zg-note">Descriptions are shown where available.</p>

  <table class="zg-table">
    <thead>
      <tr>
        <th>Program</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>CSAVGW</td>
        <td data-label="Description">Averages and performs QC on CSAMT/NSAMT electromagnetic data.</td>
      </tr>
      <tr>
        <td>TDAVGW</td>
        <td data-label="Description">&mdash;</td>
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
        <td>HEMAVGW</td>
        <td data-label="Description">&mdash;</td>
      </tr>
      <tr>
        <td>MTFT</td>
        <td data-label="Description">&mdash;</td>
      </tr>
      <tr>
        <td>MTEDIT</td>
        <td data-label="Description">Reviewing and averaging magnetotelluric impedance data.</td>
      </tr>
      <tr>
        <td>SCS2D</td>
        <td data-label="Description">&mdash;</td>
      </tr>
      <tr>
        <td>TS2DIP</td>
        <td data-label="Description">&mdash;</td>
      </tr>
      <tr>
        <td>SCSINV</td>
        <td data-label="Description">&mdash;</td>
      </tr>
      <tr>
        <td>STEMINV</td>
        <td data-label="Description">&mdash;</td>
      </tr>
      <tr>
        <td>ASTATIC</td>
        <td data-label="Description">&mdash;</td>
      </tr>
    </tbody>
  </table>
</div>
