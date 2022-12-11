<template>
  <base-navbar class="navbar-main px-0 mx-3 shadow-none">
    <div class="container-fluid py-1 px-3">
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
          <li class="breadcrumb-item text-sm">
            <router-link :to="{ name: 'home_view' }">
              Home
            </router-link>
          </li>
      
          <li class="breadcrumb-item text-sm text-dark active" aria-current="page">
            {{ $route.meta.title }}
          </li>
        </ol>
      
        <h6 class="font-weight-bolder mb-0">
          {{ $route.meta.title }}
        </h6>
      </nav>

      <div id="navbar" class="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4">
        <ul class="navbar-nav ms-auto justify-content-end">
          <li class="nav-item d-flex align-items-center">
            <base-dropdown-button :items="campaignChoices" button-name="Start campaign" button-classes="btn btn-primary btn-sm mb-0 me-3" />
          </li>
      
          <li class="nav-item d-flex align-items-center">
            <router-link :to="{ name: 'home_view' }" class="nav-link text-body fw-bold px-0">
              Sign In
            </router-link>
          </li>
      
          <li class="nav-item d-xl-none ps-3 d-flex align-items-center">
            <a id="iconNavbarSidenav" href="javascript:;" class="nav-link text-body p-0">
              <div class="sidenav-toggler-inner">
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
              </div>
            </a>
          </li>
      
          <li class="nav-item px-3 d-flex align-items-center">
            <router-link :to="{ name: 'home_view' }" class="nav-link text-body p-0">
              <font-awesome-icon icon="fa-solid fa-cog" />
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </base-navbar>
  <!-- <nav id="navbarBlur" class="navbar navbar-main navbar-expand-lg px-0 mx-4 shadow-none border-radius-xl">
    <div class="container-fluid py-1 px-3">
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb bg-transparent mb-0 pb-0 pt-1 px-0 me-sm-6 me-5">
          <li class="breadcrumb-item text-sm">
            <router-link :to="{ name: 'home_view' }">
              Home
            </router-link>
          </li>

          <li class="breadcrumb-item text-sm text-dark active" aria-current="page">
            {{ $route.meta.title }}
          </li>
        </ol>

        <h6 class="font-weight-bolder mb-0">
          {{ $route.meta.title }}
        </h6>
      </nav>

      <div id="navbar" class="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4">
        <ul class="navbar-nav ms-auto justify-content-end">
          <li class="nav-item d-flex align-items-center">
            <base-dropdown-button :items="campaignChoices" button-name="Start campaign" button-classes="btn btn-primary btn-sm mb-0 me-3" />
          </li>
          
          <li class="nav-item d-flex align-items-center">
            <router-link :to="{ name: 'home_view' }" class="nav-link text-body fw-bold px-0">
              Sign In
            </router-link>
          </li>

          <li class="nav-item d-xl-none ps-3 d-flex align-items-center">
            <a id="iconNavbarSidenav" href="javascript:;" class="nav-link text-body p-0">
              <div class="sidenav-toggler-inner">
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
                <i class="sidenav-toggler-line"></i>
              </div>
            </a>
          </li>

          <li class="nav-item px-3 d-flex align-items-center">
            <router-link :to="{ name: 'home_view' }" class="nav-link text-body p-0">
              <font-awesome-icon icon="fa-solid fa-cog" />
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav> -->
</template>

<script>
import BaseNavbar from '@/layouts/bootstrap/nav/BaseNavbar.vue'
import BaseDropdownButton from '@/layouts/bootstrap/BaseDropdownButton.vue'

export default {
  name: 'DashboardNav',
  components: {
    BaseNavbar,
    BaseDropdownButton
  },
  data () {
    return {
      campaignChoices: [
        {
          name: 'A'
        },
        {
          name: 'B'
        }, 
        {
          name: 'C'
        }
      ]
    }
  }
}
</script>
