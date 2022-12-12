<template>
  <section>
    <div class="row">
      <dashboard-page-header title="Queue" />

      <!-- Navigation -->
      <div class="col-12 my-3">
        <base-nav-pills :items="navpillChoices" @current-tab="changePage" />
      </div>

      <!-- Content -->
      <div class="row">
        <div v-if="store.actions.length === 0" class="col-8">
          <p>Aucune action en file d'attente pour le moment</p>
        </div>

        <div v-else class="col-8">
          <base-card>
            <template #body>
              <base-list-group>
                <base-list-group-item v-for="action in actions" :key="action.id" class="d-flex justify-content-between align-items-center">
                  <div class="info">
                    <span :class="actionColor(action.name)" class="fw-bold">{{ action.name }}</span> /
                    <span>{{ action.url }}</span>
                  </div>
                  <div class="badge badge-pill badge-success">
                    Completed
                  </div>
                </base-list-group-item>
              </base-list-group>
            </template>
          </base-card>
        </div>

        <!-- Limits -->
        <aside id="limits" class="col-4 d-none">
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
        </aside>
      </div>
    </div>
  </section>
</template>

<script>
import { useCampaigns } from '@/store/campaigns'
import { mapState } from 'pinia'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseListGroup from '@/layouts/bootstrap/listgroup/BaseListGroup.vue'
import BaseListGroupItem from '@/layouts/bootstrap/listgroup/BaseListGroupItem.vue'
import BaseNavPills from '@/layouts/bootstrap/nav/BaseNavPills.vue'
import DashboardPageHeader from '@/components/DashboardPageHeader.vue'

export default {
  name: 'QueueView',
  components: {
    BaseCard,
    BaseListGroup,
    BaseListGroupItem,
    BaseNavPills,
    DashboardPageHeader
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
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
  computed: {
    ...mapState(useCampaigns, ['actions'])
  },
  beforeMount () {
    this.store.loadFromCache(this.$route.params.id)
  },
  methods: {
    changePage (index) {
      index
    },
    actionColor (name) {
      if (name === 'GET') {
        return 'text-primary'
      }

      if (name === 'POST') {
        return 'text-danger'
      }

      return 'text-primary'
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
