<template>
  <section>
    <div class="row">
      <div class="col-sm-12 col-md-12">
        <base-template-card>
          <div class="card-body d-flex justify-content-between align-items-center">
            <h2 class="fw-bold"><router-link :to="{ name: 'campaigns_view' }" class="text-primary">Campaign</router-link> / {{ currentCampaign.name }}</h2>
            <div class="btn-group">
              <button type="button" class="btn btn-primary">Play</button>
              <button type="button" class="btn btn-primary">Play</button>
            </div>
          </div>
        </base-template-card>
      </div>

      <div class="col-sm-12 col-md-4 mt-2">
        <base-template-card>
          <div class="card-body">
            Google
          </div>
        </base-template-card>
      </div>

      <div class="col-sm-12 col-md-8 mt-2">
        <base-template-card>
          <div class="card-body">
            <table class="table"></table>
          </div>
        </base-template-card>
      </div>
    </div>
  </section>
</template>

<script>
import { useCampaigns } from '@/store/campaigns'
import { mapState } from 'pinia'

import BaseTemplateCard from '@/layouts/bootstrap/cards/BaseTemplateCard.vue'

export default {
  name: 'CampaignView',
  components: {
    BaseTemplateCard
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  computed: {
    ...mapState(useCampaigns, ['currentCampaign'])
  },
  beforeMount () {
    this.store.loadFromCache(this.$route.params.id)
  }
}
</script>
