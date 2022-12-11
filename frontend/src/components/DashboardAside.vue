<template>
  <aside class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start ms-3 bg-gradient-dark" id="sidenav-main">
    <div class="sidenav-header">
      <i id="iconSidenav" class="fas fa-times p-3 cursor-pointer text-white opacity-5 position-absolute end-0 top-0 d-none d-xl-none" aria-hidden="true"></i>
      <router-link :to="{ name: 'home_view' }" class="navbar-brand m-0">
        <!-- <img :src="require('@/assets/img/logo-ct.png')" class="navbar-brand-img h-100" alt="main_logo" /> -->
        <span class="ms-1 font-weight-bold text-white">Material Dashboard 2</span>
      </router-link>
    </div>

    <hr class="horizontal light mt-0 mb-2" />

    <div id="sidenav-collapse-main" class="collapse navbar-collapse w-auto">
      <ul class="navbar-nav">
        <template v-for="(link, i) in links">
          <li v-if="link.section" :key="i" class="nav-item mt-3">
            <h6 class="ps-4 ms-2 text-uppercase text-xs text-white font-weight-bolder opacity-8">
              {{ link.section }}
            </h6>
          </li>

          <template v-else>
            <li v-for="(item, y) in link.items" :key="y" class="nav-item">
              <router-link :to="{ name: item.to }" class="nav-link text-white">
                <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                  <!-- <i class="material-icons opacity-10">dashboard</i> -->
                </div>
            
                <span class="nav-link-text ms-1">{{ item.name }}</span>
              </router-link>
            </li>
          </template>
        </template>
      </ul>
    </div>

    <div class="sidenav-footer position-absolute w-100 bottom-0">
      <div class="mx-3">
        <router-link :to="{ name: 'home_view'}" class="btn bg-gradient-primary mt-4 w-100">
          Upgrade to pro
        </router-link>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'DashboardAside',
  components: {
  },
  data () {
    return {
      links: [
        {
          section: null,
          items: [
            {
              to: 'home_view',
              name: 'Home'
            },
            {
              to: 'home_view',
              name: 'Prospects'
            },
            {
              to: 'campaigns_view',
              name: 'Campaigns'
            },
            {
              to: 'queue_view',
              name: 'Queue'
            },
            {
              to: 'home_view',
              name: 'Settings'
            }
          ]
        }
      ]
    }
  }
}
</script>
