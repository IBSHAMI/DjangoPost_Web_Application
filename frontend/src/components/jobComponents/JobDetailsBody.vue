<template>
  <div class="card-body border-top">
    <h4 class="mb-4 card-title">Job Description</h4>
    <p class="mb-4 para">
      {{ bodyData.description }}
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
              <td>
                <span class="property"> {{ bodyData.type }}</span>
              </td>
            </tr>

            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Montly Salary (USD)</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ bodyData.salary }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Application Type</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ getApplicationType }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Posted date</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property">{{ formattedDate }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Remote</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property">{{ checkRemote }}</span>
              </td>
            </tr>
          </tbody>
          <tbody class="col-lg-12 col-xl-6 p-0">
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Experience</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ bodyData.experience }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Languages</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ bodyData.language }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Location</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ bodyData.location }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Number of positions</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ bodyData.numberOfPositions }}</span>
              </td>
            </tr>
            <tr>
              <td class="w-150 px-0">
                <span class="font-weight-semibold">Company</span>
              </td>
              <td><span class="separator">:</span></td>
              <td>
                <span class="property"> {{ bodyData.companyName }}</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "JobDetailsBody",
  props: ["bodyData"],
  computed: {
    formattedDate() {
      return moment(this.bodyData.created_at).format("DD MMM YYYY");
    },
    getApplicationType() {
      return this.bodyData.internal ? "Easy Apply" : "External Apply";
    },
    checkRemote() {
      return this.bodyData.remote ? "Yes" : "No";
    },
  },
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
