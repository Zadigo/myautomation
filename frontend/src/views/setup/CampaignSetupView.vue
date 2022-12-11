<template>
  <section id="campaign-setup-1">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6">
          <base-card>
            <template #body>
              <p>Build your {{ store.selectedCampaignSetup.name }} and start scrapping the web</p>
              <base-input id="campaign-name" v-model="newCampaign.name" placeholder="Campaign name" />
            </template>
          </base-card>
        </div>

        <div class="col-sm-12 col-md-6">
          <base-card>
            <template #body>
              <base-input id="campaign-url" v-model="newCampaign.url" placeholder="Campaign url" />
              <router-link :to="{ name: 'campaign_setup_settings_view', params: { id: 1 } }" class="btn btn-primary">
                Next
              </router-link>
            </template>
          </base-card>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapWritableState } from 'pinia'
import { useCampaigns } from '@/store/campaigns'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'

export default {
  components: {
    BaseCard,
    BaseInput
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  computed: {
    ...mapWritableState(useCampaigns, ['newCampaign'])
  },
  created () {
    this.store.useCampaignSetup(this.$route.params.id)
  }
}
</script>
