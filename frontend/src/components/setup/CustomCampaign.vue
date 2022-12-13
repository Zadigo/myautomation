<doc>
  When the user creates a campaign for a random
  website that is not a social media type
</doc>

<template>
  <section>
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6">
          <base-card>
            <template #body>
              <label for="select-section" class="fw-bold">Choose the section of the page to parse</label>
              <base-input id="select-section" v-model="store.newCampaign.section_to_parse" :disabled="store.newCampaign.parse_all_tables || store.newCampaign.parse_all_text" />

              <div class="mt-4">
                <base-checkbox id="select-parse-all-tables" v-model="store.newCampaign.parse_all_tables" :disabled="store.newCampaign.parse_all_text" label="Parse all the tables on the page" is-switch />
                <base-checkbox id="select-parse-all-text" v-model="store.newCampaign.parse_all_text" :disabled="store.newCampaign.parse_all_tables" class="my-3" label="Parse all the text on the page" is-switch />
                <p v-if="store.newCampaign.parse_all_text" class="alert alert-info my-2">
                  <font-awesome-icon icon="fa-solid fa-circle-info" class="me-2" />
                  Choosing this option might have the scrapper return some incoherent items
                  in your dataset
                </p>
              </div>
            </template>

            <template #footer>
              <button type="button" class="btn btn-primary" @click="goToPrevious({ name: 'campaign_setup_view', params: { id: $route.params.id } })">
                <font-awesome-icon icon="fa-solid fa-arrow-left" class="me-2" />
                Back
              </button>

              <button type="button" class="btn btn-primary mx-2" @click="goToNext({ name: 'campaign_setup_settings_view', params: { id: $route.params.id } })">
                Next
                <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
              </button>
            </template>
          </base-card>
        </div>

        <div class="col-sm-12 col-md-6">
          <conditions-group />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { useCampaigns } from '@/store/campaigns'
import { useNavigation } from '@/composables/navigation'
import { getCurrentInstance } from 'vue'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'
import ConditionsGroup from '../conditions/ConditionsGroup.vue'

export default {
  name: 'CustomCampaign',
  components: {
    BaseCard,
    BaseCheckbox,
    BaseInput,
    ConditionsGroup
  },
  setup () {
    const app = getCurrentInstance()
    const { goToNext, goToPrevious } = useNavigation(app)
    const store = useCampaigns()
    return {
      store,
      goToPrevious,
      goToNext
    }
  }
}
</script>
