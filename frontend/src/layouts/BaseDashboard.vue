<template>
  <!-- Aside -->
  <dashboard-aside />
  
  <!-- Main -->
  <main class="main-content border-radius-lg">
    <!-- Nav -->
    <dashboard-nav />

    <!-- Content -->
    <div class="container-fluid py-4">
      <router-view></router-view>

      <!-- Footer -->
      <!-- <footer class="footer py-4">
        <div class="container-fluid">
          <div class="row align-items-center justify-content-lg-between">
            <div class="col-lg-6 mb-lg-0 mb-4">
              <div class="copyright text-center text-sm text-muted text-lg-start">
                © 1974
                , made with <i class="fa fa-heart"></i> by
                <a href="https://www.creative-tim.com" class="font-weight-bold" target="_blank" rel="noopener noreferrer">Creative Tim</a>
                for a better web.
              </div>
            </div>
            <div class="col-lg-6">
              <ul class="nav nav-footer justify-content-center justify-content-lg-end">
                <li class="nav-item">
                  <a href="https://www.creative-tim.com" class="nav-link text-muted" target="_blank" rel="noopener noreferrer">Creative Tim</a>
                </li>
                <li class="nav-item">
                  <a href="https://www.creative-tim.com/presentation" class="nav-link text-muted" target="_blank" rel="noopener noreferrer">About Us</a>
                </li>
                <li class="nav-item">
                  <a href="https://www.creative-tim.com/blog" class="nav-link text-muted" target="_blank" rel="noopener noreferrer">Blog</a>
                </li>
                <li class="nav-item">
                  <a href="https://www.creative-tim.com/license" class="nav-link pe-0 text-muted" target="_blank" rel="noopener noreferrer">License</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </footer> -->
    </div>
  </main>
</template>

<script>
import DashboardAside from '@/components/DashboardAside.vue'
import DashboardNav from '@/components/DashboardNav.vue'

export default {
  name: 'BaseDashboard',
  components: {
    DashboardAside,
    DashboardNav
  }
}
</script>
