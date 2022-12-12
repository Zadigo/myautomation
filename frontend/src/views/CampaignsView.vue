<template>
  <section>
    <div class="row">
      <dashboard-page-header title="Campaigns">
        <button type="button" class="btn btn-info" @click="showListCampaigns = !showListCampaigns">
          <font-awesome-icon icon="fa-solid fa-hourglass-start" class="me-2" />
          Start a campaign
        </button>
      </dashboard-page-header>

      <div class="col-12 my-3">
        <base-nav-pills :items="navpillChoices" @current-tab="changePage" />
      </div>

      <!-- Content -->
      <div v-if="campaigns.length === 0" class="col-sm-12 col-md-7 offset-md-2 text-center my-3">
        <img :src="require('@/assets/computer.png')" width="200" height="200" class="img-fluid" alt="Create campaign">
        <h3 class="fw-bold my-4">You have no campaigns yet</h3>
        <button type="button" class="btn btn-lg btn-info" @click="showListCampaigns = !showListCampaigns">
          <font-awesome-icon icon="fa-solid fa-hourglass-start" class="me-2" />
          Start a campaign
        </button>
      </div>
      
      <div v-else class="col-12">
        <base-card>
          <template #body>
            <base-list-group>
              <base-list-group-item-action v-for="campaign in sortedCampaigns" :key="campaign.id" class="d-flex justify-content-between align-items-center p-3">
                <span @click="goToCampaign(campaign)">{{ campaign.name }}</span>
                <button type="button" class="btn btn-sm btn-light m-0 btn-float shadow-none" @click="launchCampaign(campaign)">
                  <font-awesome-icon v-if="campaign.paused || !campaign.runned" icon="fa-solid fa-play" />
                  <font-awesome-icon v-else icon="fa-solid fa-stop" />
                  <base-spinner color="dark" size="sm" class="d-none" />
                </button>
              </base-list-group-item-action> 
            </base-list-group>
          </template>
        </base-card>
      </div>

      <!-- Modals -->
      <modal-list-campaigns id="setup-campaign" :show="showListCampaigns" size="xl" @close="showListCampaigns = false" />
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'pinia'
import { useCampaigns } from '@/store/campaigns'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseNavPills from '@/layouts/bootstrap/nav/BaseNavPills.vue'
import DashboardPageHeader from '@/components/DashboardPageHeader.vue'
import BaseListGroup from '@/layouts/bootstrap/listgroup/BaseListGroup.vue'
import BaseListGroupItemAction from '@/layouts/bootstrap/listgroup/BaseListGroupItemAction.vue'
import BaseSpinner from '@/layouts/bootstrap/BaseSpinner.vue'
import ModalListCampaigns from '@/components/ModalListCampaigns.vue'

export default {
  name: 'CampaignsView',
  components: {
    BaseCard,
    BaseListGroup,
    BaseListGroupItemAction,
    BaseNavPills,
    BaseSpinner,
    DashboardPageHeader,
    ModalListCampaigns
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  data () {
    return {
      showListCampaigns: false,
      currentTab: 0,
      navpillChoices: [
        {
          name: 'En cours'
        },
        {
          name: 'En pause'
        },
        {
          name: 'Brouillon'
        },
        {
          name: 'Archivee'
        }
      ]
    }
  },
  computed: {
    ...mapState(useCampaigns, ['campaigns']),
    paused () {
      // Campaigns that were runned at least once
      // and then paused afterwards
      return _.filter(this.campaigns, (item) => {
        return item.runned && item.paused
      })
    },
    drafts () {
      return _.filter(this.campaigns, ['draft', true])
    },
    countPaused () {
      return this.paused.length
    },
    sortedCampaigns () {
      let items
      switch (this.currentTab) {
        case 0:
          items = this.campaigns
          break

        case 1:
          items = this.paused
          break

        case 2:
          items = this.drafts
          break
        
        case 3:
          items = _.filter(this.campaigns, ['archived', true])
          break
      
        default:
          items = this.campaigns
          break
      }
      return items
    }
  },
  beforeMount () {
    this.getCampaigns()
  },
  methods: {
    async getCampaigns () {
      // Get all the campaigns created by
      // the user
      try {
        const cachedCampaigns = this.$session.retrieve('cachedCampaigns')
        if (!cachedCampaigns) {
          const response = await this.$http.get('campaigns/list')
          this.$session.create('cachedCampaigns', response.data)
          this.store.updateCampaigns(response.data)
        } else {
          this.store.updateCampaigns(cachedCampaigns)
        }

      } catch (error) {
        console.error(error)
      }
    },
    async launchCampaign (campaign) {
      campaign.paused = !campaign.paused
      campaign.archived = false
      campaign.draft = false
      campaign.runned = true
      try {
        await this.$http.post('campaigns/state', {
          pause: campaign.paused,
          archived: campaign.archived,
          draft: false,
          runned: campaign.runned
        })
      } catch (error) {
        console.error(error)
      }
    },
    changePage (index) {
      this.currentTab = index
    },
    goToCampaign (campaign) {
      this.store.setCurrentCampaign(campaign)
      this.$router.push({ name: 'campaign_view', params: { id: campaign.id } })
    }
  }
}
</script>
