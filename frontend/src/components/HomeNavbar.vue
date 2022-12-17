<template>
  <header class="header-global">
    <nav
      id="navbar-main"
      aria-label="Primary navigation"
      class="navbar navbar-main navbar-expand-lg navbar-theme-primary headroom navbar-light"
    >
      <div class="container position-relative">
        <a class="navbar-brand me-lg-5" href="../../index.html">
          <img
            class="navbar-brand-light"
            src="../../assets/img/brand/dark.svg"
            alt="Logo dark"
          />
        </a>
        <div class="navbar-collapse collapse me-auto" id="navbar_global">
          <div class="navbar-collapse-header">
            <div class="row">
              <div class="col-6 collapse-close">
                <a
                  href="#navbar_global"
                  class="fas fa-times"
                  data-bs-toggle="collapse"
                  data-bs-target="#navbar_global"
                  aria-controls="navbar_global"
                  aria-expanded="false"
                  title="close"
                  aria-label="Toggle navigation"
                ></a>
              </div>
            </div>
          </div>
          <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
            <li class="nav-item dropdown">
              <a href="#" class="nav-link">Pages</a>
            </li>
            <li class="nav-item dropdown">
              <a href="#" class="nav-link">Dashboard</a>
            </li>
          </ul>
        </div>
        <div class="d-flex align-items-center">
          <a
            href=""
            target="_blank"
            class="btn btn-outline-gray-100 d-none d-lg-inline me-md-3"
          >
            Docs</a
          >
          <a href="" target="_blank" class="btn btn-primary">Download</a>
          <button
            class="navbar-toggler ms-2"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbar_global"
            aria-controls="navbar_global"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "HomeNavbar",
};
</script>

<style></style>
