<template>
  <section>
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="alert alert-info text-center">
            <h1>This section will be coming soon!</h1>
            <router-link :to="{ name: 'campaigns_view' }" class="btn btn-lg btn-primary mt-3">
              <font-awesome-icon icon="fa-solid fa-star" class="me-2" />
              Create your first campaign
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="row">
      <div class="col-12 position-relative z-index-2">
        <div class="card card-plain mb-4">
          <div class="card-body p-3">
            <div class="row">
              <div class="col-lg-6">
                <div class="d-flex flex-column h-100">
                  <h2 class="font-weight-bolder mb-0">
                    General Statistics
                  </h2>
                </div>
              </div>
            </div>
          </div>
        </div>
  
        <div class="row">
          <div class="col-lg-6 col-sm-5">
            <div class="card mb-5">
              <div class="card-header p-3 pt-2">
                <div class="icon icon-lg icon-shape bg-gradient-dark shadow-dark shadow text-center border-radius-xl mt-n4 position-absolute">
                  <i class="material-icons opacity-10">weekend</i>
                </div>

                <div class="text-end pt-1">
                  <p class="text-sm mb-0 text-capitalize">Bookings</p>
                  <h4 class="mb-0">281</h4>
                </div>
              </div>
  
              <hr class="dark horizontal my-0" />
              <div class="card-footer p-3">
                <p class="mb-0">
                  <span class="text-success text-sm font-weight-bolder">+55% </span>than last week
                </p>
              </div>
            </div>
  
            <div class="card mb-5">
              <div class="card-header p-3 pt-2">
                <div class="icon icon-lg icon-shape bg-gradient-primary shadow-primary shadow text-center border-radius-xl mt-n4 position-absolute">
                  <i class="material-icons opacity-10">leaderboard</i>
                </div>

                <div class="text-end pt-1">
                  <p class="text-sm mb-0 text-capitalize">Today's Users</p>
                  <h4 class="mb-0">2,300</h4>
                </div>
              </div>
  
              <hr class="dark horizontal my-0" />
              <div class="card-footer p-3">
                <p class="mb-0">
                  <span class="text-success text-sm font-weight-bolder">+3% </span>than last month
                </p>
              </div>
            </div>
          </div>

          <div class="col-lg-6 col-sm-5 mt-sm-0 mt-4">
            <div class="card mb-5">
              <div class="card-header p-3 pt-2 bg-transparent">
                <div class="icon icon-lg icon-shape bg-gradient-success shadow-success text-center border-radius-xl mt-n4 position-absolute">
                  <i class="material-icons opacity-10">store</i>
                </div>
                <div class="text-end pt-1">
                  <p class="text-sm mb-0 text-capitalize">Revenue</p>
                  <h4 class="mb-0">34k</h4>
                </div>
              </div>
  
              <hr class="horizontal my-0 dark" />
              <div class="card-footer p-3">
                <p class="mb-0">
                  <span class="text-success text-sm font-weight-bolder">+1% </span>than yesterday
                </p>
              </div>
            </div>
              
            <base-template-card>
              <div class="card-header p-3 pt-2 bg-transparent">
                <div class="icon icon-lg icon-shape bg-gradient-info shadow-info text-center border-radius-xl mt-n4 position-absolute">
                  <i class="material-icons opacity-10">person_add</i>
                </div>
                <div class="text-end pt-1">
                  <p class="text-sm mb-0 text-capitalize">Followers</p>
                  <h4 class="mb-0">+91</h4>
                </div>
              </div>

              <hr class="horizontal my-0 dark" />
              <div class="card-footer p-3">
                <p class="mb-0">Just updated</p>
              </div>
            </base-template-card>
          </div>
        </div>
  
        <div class="row mt-4">
          <div class="col-12">
            <div class="card mb-4">
              <div class="d-flex">
                <div class="icon icon-shape icon-lg bg-gradient-success shadow text-center border-radius-xl mt-n3 ms-4">
                  <i class="material-icons opacity-10" aria-hidden="true">language</i>
                </div>
                <h6 class="mt-3 mb-2 ms-3">Sales by Country</h6>
              </div>

              <div class="card-body p-3">
                <div class="row">
                  <div class="col-lg-6 col-md-7">
                    <div class="table-responsive">

                    </div>
                  </div>

                  <div class="col-lg-6 col-md-5">
                    <div id="map" class="mt-0 mt-lg-n4"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  
    <div class="row mt-4">
      <div class="col-lg-5 mb-lg-0 mb-4">
        <div class="card z-index-2 mt-4">
          <div class="card-body mt-n5 px-3">
            <div class="bg-gradient-dark shadow-dark border-radius-lg py-3 pe-1 mb-3">
              <div class="chart">
                <canvas id="chart-bars" class="chart-canvas" height="170"></canvas>
              </div>
            </div>
            <h6 class="ms-2 mt-4 mb-0">Active Users</h6>
            <p class="text-sm ms-2">
              (<span class="font-weight-bolder">+11%</span>) than last week
            </p>
            <div class="container border-radius-lg">
              <div class="row">
                <div class="col-3 py-3 ps-0">
                  <div class="d-flex mb-2">
                    <div class="icon icon-shape icon-xxs shadow border-radius-sm bg-gradient-primary text-center me-2 d-flex align-items-center justify-content-center">
                      <i class="material-icons opacity-10">groups</i>
                    </div>
                    <p class="text-xs my-auto font-weight-bold">Users</p>
                  </div>
                  <h4 class="font-weight-bolder">42K</h4>
                  <div class="progress w-75">
                    <div class="progress-bar bg-dark w-60" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
                  </div>
                </div>
                <div class="col-3 py-3 ps-0">
                  <div class="d-flex mb-2">
                    <div class="icon icon-shape icon-xxs shadow border-radius-sm bg-gradient-info text-center me-2 d-flex align-items-center justify-content-center">
                      <i class="material-icons opacity-10">ads_click</i>
                    </div>
                    <p class="text-xs mt-1 mb-0 font-weight-bold">Clicks</p>
                  </div>
                  <h4 class="font-weight-bolder">1.7m</h4>
                  <div class="progress w-75">
                    <div class="progress-bar bg-dark w-90" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                  </div>
                </div>
                <div class="col-3 py-3 ps-0">
                  <div class="d-flex mb-2">
                    <div class="icon icon-shape icon-xxs shadow border-radius-sm bg-gradient-warning text-center me-2 d-flex align-items-center justify-content-center">
                      <i class="material-icons opacity-10">receipt</i>
                    </div>
                    <p class="text-xs mt-1 mb-0 font-weight-bold">Sales</p>
                  </div>
                  <h4 class="font-weight-bolder">399$</h4>
                  <div class="progress w-75">
                    <div class="progress-bar bg-dark w-30" role="progressbar" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
                  </div>
                </div>
                <div class="col-3 py-3 ps-0">
                  <div class="d-flex mb-2">
                    <div class="icon icon-shape icon-xxs shadow border-radius-sm bg-gradient-danger text-center me-2 d-flex align-items-center justify-content-center">
                      <i class="material-icons opacity-10">category</i>
                    </div>
                    <p class="text-xs mt-1 mb-0 font-weight-bold">Items</p>
                  </div>
                  <h4 class="font-weight-bolder">74</h4>
                  <div class="progress w-75">
                    <div class="progress-bar bg-dark w-50" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="col-lg-7">
        <div class="card z-index-2">
          <div class="card-header pb-0">
            <h6>Sales overview</h6>
            <p class="text-sm">
              <i class="fa fa-arrow-up text-success"></i>
              <span class="font-weight-bold">4% more</span> in 2021
            </p>
          </div>

          <div class="card-body p-3">
            <div class="chart">
              
            </div>
          </div>
        </div>
      </div>
    </div>
  
    <div class="row">
      <div class="col-12">
        <div id="globe" class="position-absolute end-0 top-10 mt-sm-3 mt-7 me-lg-7">
          <canvas width="700" height="600" class="w-lg-100 h-lg-100 w-75 h-75 me-lg-0 me-n10 mt-lg-5"></canvas>
        </div>
      </div>
    </div> -->
  </section>
</template>


<script>
// import BaseTemplateCard from '@/layouts/bootstrap/cards/BaseTemplateCard.vue'

export default {
  name: 'IndexView',
  components: {
    // BaseTemplateCard
  }
}
</script>
