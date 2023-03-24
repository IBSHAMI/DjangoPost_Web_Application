<template>
  <div class="card-body border-top">
    <h4 class="mb-4 card-title">Job Description</h4>
    <p class="mb-4 para">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos unde ratione
      ut velit eos ducimus, cupiditate, magni, ipsum labore ab quidem quasi
      illum illo quo tempora dolorem quibusdam quisquam delectus.
    </p>
    <div class="job-overview">
      <h4 class="mb-4 card-title">Employment Information</h4>
      <div class="table-responsive">
        <table class="table row table-borderless w-100 m-0 text-nowrap">
          <tbody class="col-lg-12 col-xl-6 p-0">
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Job Type</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> Full Time</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Role</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> Hard ware Technician</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Min Salary</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> $12,000</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Max Salary</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> $15,000</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Min Exp</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property">0yrs</span></td>
            </tr>
          </tbody>
          <tbody class="col-lg-12 col-xl-6 p-0">
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Max Exp</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> 2yrs</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Languages</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> English , Hindi</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Locality</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> USA , UK , India</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Eligibility</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> Any Graduate</span></td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Company</span>
              </td>
              <td><span class="separator">:</span></td>
              <td><span class="property"> Acme Corporation pvt ltd</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "JobDetailsBody",
};
</script>

<style scoped>
.card-title {
  font-size: 1.2rem;
  font-family: var(--Nunito);
  font-weight: 500;
  line-height: 1.5;
  color: var(----primary-color-1);
}

.job-overview {
  border: thin solid #e0e6f7;
  border-radius: 8px;
  padding: 20px 30px 30px 30px;
  margin-bottom: 50px;
}

.font-weight-semibold {
  font: normal italic 600 14px/25px var(--Nunito);
  color: var(----primary-color-1);
}

.separator {
  font: normal 700 14px/25px var(--Nunito);
  color: var(----primary-color-1);
}

.property {
  font: normal 400 14px/25px var(--Nunito);
  color: var(----primary-color-1);
}
</style>
