<template>
  <div class="mx-auto py-auto">
    <ul class="pagination m-3 pb-5">
      <li class="page-item page-prev disabled">
        <a class="page-link" href="javascript:void(0);" tabindex="-1">Prev</a>
      </li>
      <li class="page-item active">
        <a class="page-link" href="javascript:void(0);">1</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="javascript:void(0);">2</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="javascript:void(0);">3</a>
      </li>
      <li class="page-item page-next">
        <a class="page-link" href="javascript:void(0);">Next</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "PaginationItem",
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
