<template>
  <section>
    <div class="row">
      <div class="col-sm-12 col-md-8">
        <base-card>
          <template #body>
            <!-- Results per search -->
            <p class="fw-bold">Number of results to scrape per search</p>
            <div class="w-50">
              <base-input id="campaign-settings" v-model="store.newCampaign.results_per_search" type="number" min="1" placeholder="100" />
            </div>
    
            <div class="alert alert-info my-4">
              Pick at least one item you would like to scrape.
            </div>
    
            <base-list-group-checkbox :items="scrapChoices" @list-group-selection="handleSelection" />
          </template>
          
          <template #footer>
            <router-link :to="{ name: 'campaign_setup_view', params: { id: $route.params.id } }" class="btn btn-primary">
              <font-awesome-icon icon="fa-solid fa-arrow-left" class="me-2" />
              Back
            </router-link>
            
            <button type="button" class="btn btn-primary mx-2" @click="createCampaign">
              Create campaign
              <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
            </button>
          </template>
        </base-card>
      </div>

      <div class="col-sm-12 col-md-4">
        <base-card>
          <template #body>
            <p class="fw-bold">Proxies</p>
            <base-input id="select-proxies" placeholder="Type a list of proxies separated by commas" />
            <p class="fw-bold mt-4">Maximum number of retries</p>
            <base-input id="select-proxies" min="0" max="10" />
          </template>
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import { useCampaigns } from '@/store/campaigns'

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
    const store = useCampaigns()
    return {
      store
    }
  },
  data () {
    return {
      scrapChoices: [
        {
          name: 'Everything',
          subtitle: 'Return all available data from the website'
        },
        {
          name: 'Emails',
          subtitle: 'Get emails alone'
        }
      ]
    }
  },
  methods: {
    createCampaign () {
      this.store.createCampaign()
      this.$router.push({ name: 'campaigns_view' })
    },
    handleSelection (value) {
      value
    }
  }
}
</script>
