<template>
  <section>
    <base-card>
      <template #body>
        <base-input id="campaign-settings" :update:initial="(value) => { newCampaign.name = value }" type="url" placeholder="URL to" />

        <router-link :to="{ name: 'campaign_setup_view', params: { id: $route.params.id } }" class="btn btn-primary">
          Back
        </router-link>

        <button type="button" class="btn btn-primary" @click="createCampaign">
          Create campaign
        </button>
      </template>
    </base-card>
  </section>
</template>

<script>
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
  methods: {
    createCampaign () {
      this.store.createCampaign()
      this.$router.push({ name: 'campaigns_view' })
    }
  }
}
</script>
