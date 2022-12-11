<template>
  <section>
    <div class="row">
      <dashboard-page-header title="Queue" />

      <div class="col-12 my-3">
        <base-nav-pills :items="navpillChoices" @current-tab="changePage" />
      </div>

      <!-- Content -->
      <div class="row">
        <div v-if="store.actions.length === 0" class="col-8">
          <p>Aucune action en file d'attente pour le moment</p>
        </div>

        <div v-else class="col-8">
          
        </div>

        <div id="limits" class="col-4">
          <h3>Quotas journaliers</h3>
          <p class="text-muted">Ces quotas sont mis à jour quotidiennement.</p>

          <base-card>
            <template #body>
              <div class="row">
                <div class="col-3">A</div>
                <div class="col-auto">
                  <p class="fw-bold m-0">Invitations</p>
                  <div class="d-flex justify-content-left align-items-baseline">
                    <div class="fw-bold fs-3">78</div>
                    <div class="ms-1">restants aujourd'hui</div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="16" aria-valuemin="0" aria-valuemax="78" style="width: 5%"></div>
                  </div>
                </div>
              </div>
            </template>
          </base-card>

          <base-card class="my-3">
            <template #body>
              <div class="row">
                <div class="col-3">A</div>
                <div class="col-auto">
                  <p class="fw-bold m-0">Invitations</p>
                  <div class="d-flex justify-content-left align-items-baseline">
                    <div class="fw-bold fs-3">78</div>
                    <div class="ms-1">restants aujourd'hui</div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="16" aria-valuemin="0" aria-valuemax="78" style="width: 10%"></div>
                  </div>
                </div>
              </div>
            </template>
          </base-card>

          <base-card>
            <template #body>
              <div class="row">
                <div class="col-3">A</div>
                <div class="col-auto">
                  <p class="fw-bold m-0">Invitations</p>
                  <div class="d-flex justify-content-left align-items-baseline">
                    <div class="fw-bold fs-3">78</div>
                    <div class="ms-1">restants aujourd'hui</div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="16" aria-valuemin="0" aria-valuemax="78" style="width: 85%"></div>
                  </div>
                </div>
              </div>
            </template>
          </base-card>

          <base-card class="my-3">
            <template #body>
              <div class="row">
                <div class="col-3">A</div>
                <div class="col-auto">
                  <p class="fw-bold m-0">Invitations</p>
                  <div class="d-flex justify-content-left align-items-baseline">
                    <div class="fw-bold fs-3">78</div>
                    <div class="ms-1">restants aujourd'hui</div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="16" aria-valuemin="0" aria-valuemax="78" style="width: 35%"></div>
                  </div>
                </div>
              </div>
            </template>
          </base-card>

          <base-card>
            <template #body>
              <div class="row">
                <div class="col-3">A</div>
                <div class="col-auto">
                  <p class="fw-bold m-0">Invitations</p>
                  <div class="d-flex justify-content-left align-items-baseline">
                    <div class="fw-bold fs-3">78</div>
                    <div class="ms-1">restants aujourd'hui</div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="16" aria-valuemin="0" aria-valuemax="78" style="width: 5%"></div>
                  </div>
                </div>
              </div>
            </template>
          </base-card>

          <base-card class="my-3">
            <template #body>
              <div class="row">
                <div class="col-3">A</div>
                <div class="col-auto">
                  <p class="fw-bold m-0">Invitations</p>
                  <div class="d-flex justify-content-left align-items-baseline">
                    <div class="fw-bold fs-3">78</div>
                    <div class="ms-1">restants aujourd'hui</div>
                  </div>
                </div>
                <div class="col-12">
                  <div class="progress">
                    <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="16" aria-valuemin="0" aria-valuemax="78" style="width: 15%"></div>
                  </div>
                </div>
              </div>
            </template>
          </base-card>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseNavPills from '@/layouts/bootstrap/nav/BaseNavPills.vue'
import DashboardPageHeader from '@/components/DashboardPageHeader.vue'
import { useCampaigns } from '@/store/campaigns'

export default {
  name: 'QueueView',
  components: {
    BaseCard,
    BaseNavPills,
    DashboardPageHeader
  },
  data () {
    return {
      navpillChoices: [
        {
          name: 'Linkedin'
        },
        {
          name: 'Email'
        }
      ]
    }
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  methods: {
    changePage (index) {
      index
    }
  }
}
</script>

<style>
#limits {
  height: 500px;
  overflow-y: scroll;
}
</style>
