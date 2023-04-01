<template>
  <footer class="bg-dark text-white py-4 footer-custom">
    <div class="container">
      <div class="row d-flex justify-content-center">
        <div class="col-md-4">
          <h5 class="mb-3">DjangoPost</h5>
          <p>
            Your go-to platform for finding the best software development jobs
            and talents in the industry.
          </p>
        </div>
        <div class="col-md-4">
          <h5 class="mb-3">Quick Links</h5>
          <ul class="list-unstyled">
            <li><a href="#home" class="text-decoration-none">Home</a></li>
            <li>
              <a href="#features" class="text-decoration-none">Features</a>
            </li>
            <li><a href="#about" class="text-decoration-none">About</a></li>
          </ul>
        </div>
        <div class="col-md-4">
          <h5 class="mb-3">Contact Us</h5>
          <p>Email: info@djangopost.com</p>
          <p>Phone: +1 123 456 7890</p>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col text-center">
          <p class="mb-0">© 2023 DjangoPost. All Rights Reserved.</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterSection",
};
</script>

<style scoped>
.footer-custom h5 {
  color: #11ab7c;
}

.footer-custom li a,
.footer-custom p {
  color: rgba(255, 255, 255, 0.5);
}
</style>
