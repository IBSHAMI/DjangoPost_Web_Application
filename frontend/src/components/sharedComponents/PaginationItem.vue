<template>
  <div class="mx-auto py-auto">
    <ul class="pagination m-3 pb-5">
      <li
        class="page-item page-prev"
        :class="{ disabled: currentPage === 1 }"
        style="cursor: pointer"
        @click="navigatePrevious"
      >
        <span class="page-link" tabindex="-1">Prev</span>
      </li>
      <li
        v-for="page in totalPages"
        class="page-item"
        :key="page"
        :class="{ active: page === currentPage }"
        style="cursor: pointer"
        @click.prevent="navigatePages(page)"
        :disabled="page === currentPage"
      >
        <span class="page-link">{{ page }}</span>
      </li>
      <li
        class="page-item page-next"
        :class="{ disabled: currentPage === totalPages }"
        style="cursor: pointer"
        @click.prevent="navigateNext"
      >
        <span class="page-link">Next</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PaginationItem",
  props: ["currentPage", "totalPages"],
  methods: {
    navigatePages(page) {
      this.$emit("navigatePages", page);
    },
    navigateNext() {
      this.$emit("navigateNext");
    },
    navigatePrevious() {
      this.$emit("navigatePrevious");
    },
  },
};
</script>

<style scoped>
.pagination {
  display: -ms-flexbox;
  display: flex;
  padding-left: 0;
  list-style: none;
  border-radius: 3px;
  --bs-pagination-color: #11ab7c;
  --bs-pagination-focus-color: #11ab7c;
  --bs-pagination-active-bg: #11ab7c;
  --bs-pagination-focus-bg: #e9ecef;
  --bs-pagination-active-border-color: #11ab7c;
  --bs-pagination-hover-color: #11ab7c;
}

.page-item {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding: 0.2rem 0.4rem;
  margin-left: -1px;
  line-height: 1.25;
  color: #11ab7c;
}

.page-item.active .page-link {
  z-index: 1;
  color: #fff;
  background-color: #11ab7c;
  border-color: #11ab7c;
}
</style>
