<template>
  <section id="campaign-setup-1">
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6">
          <base-card>
            <template #body>
              <p class="text-muted">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt 
                commodi maxime non, voluptatem fuga modi beatae perferendis totam, odit 
                rerum dicta consequatur molestiae at placeat ipsa. Eum nihil ullam necessitatibus.
              </p>
              <base-input id="campaign-name" v-model="newCampaign.name" placeholder="Campaign name" />
            </template>
          </base-card>
        </div>

        <div class="col-sm-12 col-md-6">
          <base-card>
            <template #header>
              <h5 class="m-0">How would you like to load your urls?</h5>
            </template>

            <template #body>
              <div class="row text-center">
                <div class="col-6">
                  <base-template-card id="upload-methods" :class="{ 'shadow-none': useFile }" @click="useFile = false">
                    <div class="card-body">
                      <font-awesome-icon icon="fa-solid fa-i-cursor" size="3x" class="mb-2" />
                      <p class="fw-light">Manually</p>
                    </div>
                  </base-template-card> 
                </div>
  
                <div class="col-6">
                  <base-template-card id="upload-methods" :class="{ 'shadow-none': !useFile }" @click="useFile = true">
                    <div class="card-body">
                      <font-awesome-icon icon="fa-solid fa-upload" size="3x" class="mb-2" />
                      <p class="fw-light">Upload a file</p>
                    </div>
                  </base-template-card> 
                </div>
              </div>
              
              <div v-if="!useFile" class="my-4">
                <base-input id="campaign-url" v-model="newCampaign.url" placeholder="Type the url of website to parse" class="mb-2" />
              </div>

              <div v-else class="my-4">
                <p class="text-muted">Ensure your file has the following fields: website</p>
                <base-input id="campaign-urls" v-model="newCampaign.urls_file" type="file" class="mb-2" />
              </div>


              <router-link :to="{ name: 'campaign_setup_settings_view', params: { id: 1 } }" class="btn btn-primary">
                Next
                <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
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
import BaseTemplateCard from '@/layouts/bootstrap/cards/BaseTemplateCard.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'

export default {
  components: {
    BaseCard,
    BaseTemplateCard,
    BaseInput
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  data () {
    return {
      useFile: false
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

<style scoped>
#upload-methods:hover {
  cursor: pointer;
  background-color: rgba(0, 0, 0, .075);
}
</style>
