<template>
  <section>
    <div class="row">
      <div class="col-sm-12 col-md-8">
        <base-card>
          <template #body>
            <!-- Results per search -->
            <p class="fw-bold">Number of results to scrape per search</p>
            <div class="w-50">
              <base-input id="campaign-reasults-per-search" v-model="store.newCampaign.results_per_search" type="number" min="1" placeholder="100" />
            </div>
    
            <div class="alert alert-info my-4">
              <font-awesome-icon icon="fa-solid fa-info-circle" class="me-2" />
              Pick at least one item that you would like to scrape. Note that only
              the selected items will be returned when selecting one or many of
              these options
            </div>
    
            <base-list-group-checkbox id="scrap-choices" :items="scrapChoices" @list-group-selection="handleSelection" />
          </template>
        </base-card>
      </div>

      <div class="col-sm-12 col-md-4">
        <base-card>
          <template #body>
            <p class="fw-bold">Proxies</p>
            <base-input id="select-proxies" v-model="store.newCampaign.proxies" placeholder="Type a list of proxies separated by commas" />
            
            <p class="fw-bold mt-4">Maximum number of retries</p>
            <base-input id="select-retries" v-model="store.newCampaign.retries" min="0" max="10" />
          </template>
        </base-card>
      </div>

      <div class="col-sm-12 col-md-12 mt-2">
        <base-card>
          <template #body>
            <button type="button" class="btn btn-primary" @click="goToPrevious({ name: 'custom_campaign_setup_view', params: { id: $route.params.id } })">
              <font-awesome-icon icon="fa-solid fa-arrow-left" class="me-2" />
              Back
            </button>
          
            <button type="button" class="btn btn-secondary mx-2" @click="createCampaign">
              <font-awesome-icon icon="fa-solid fa-cloud-arrow-up" class="me-2" />
              Save draft
            </button>

            <button type="button" class="btn btn-primary mx-2" @click="createCampaign(false)">
              Create campaign
              <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
            </button>
          </template>
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import { useCampaigns } from '@/store/campaigns'
import { getCurrentInstance } from 'vue'
import { useNavigation } from '@/composables/navigation'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'
import BaseListGroupCheckbox from '@/layouts/bootstrap/listgroups/BaseListGroupCheckbox.vue'

export default {
  components: {
    BaseCard,
    BaseInput,
    BaseListGroupCheckbox
  },
  setup () {
    const app = getCurrentInstance()
    const { goToPrevious } = useNavigation(app)
    const store = useCampaigns()
    return {
      store,
      goToPrevious
    }
  },
  data () {
    return {
      scrapChoices: [
        {
          name: 'Emails',
          subtitle: 'Get emails'
        },
        {
          name: 'Telephone',
          subtitle: 'Get telephone numbers'
        }
      ]
    }
  },
  methods: {
    async createCampaign (draft = true) {
      // Create a new campaign
      try {
        this.store.newCampaign.draft = draft
        const response = await this.$http.post('campaigns/create', this.store.newCampaign)
        this.store.updateCampaigns(response.data)
        this.$session.remove('newCampaign')
        this.store.resetNewCampaign()
        this.$router.push({ name: 'campaigns_view' })
      } catch (error) {
        console.log(error)
      }
    },
    handleSelection (value) {
      value
    }
  }
}
</script>
