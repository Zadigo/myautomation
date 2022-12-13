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
              
              <div class="mt-4">
                <div class="alert alert-info">
                  <font-awesome-icon icon="fa-solid fa-info-circle" class="me-2" />
                  You can load a campaign that you previously started and continue editing it
                </div>
                <button type="button" class="btn btn-info mt-1 disabled">Load started campaign</button>
              </div>
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
                <base-input id="campaign-urls" v-model="newCampaign.urls" placeholder="Url of the website to parse" class="mb-2" />

                <div class="alert alert-danger mt-2 d-none">
                  <font-awesome-icon icon="fa-solid fa-info-circle" class="me-2" />
                  <a href>Some websites</a> are not handled. You need to change the url and choose
                  from the list of valid websites to tuse
                </div>
              </div>

              <div v-else class="my-4">
                <p class="text-muted">Ensure your file has the following fields: website</p>
                <input id="campaign-csv-file" type="file" class="form-control" @change="handleUpload($event)">
              </div>

              <button type="button" class="btn btn-primary" @click="goToNext({ name: 'custom_campaign_setup_view', params: { id: $route.params.id } })">
                Next
                <font-awesome-icon icon="fa-solid fa-arrow-right" class="ms-2" />
              </button>
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
import { getCurrentInstance } from 'vue'
import { useNavigation } from '@/composables/navigation'

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
    const app = getCurrentInstance()
    const { goToNext } = useNavigation(app)
    const store = useCampaigns()
    return {
      store,
      goToNext
    }
  },
  data () {
    return {
      useFile: false
    }
  },
  computed: {
    ...mapWritableState(useCampaigns, ['newCampaign']),
    hasInvalidUrls () {
      return false
    }
  },
  created () {
    this.store.useCampaignSetup(this.$route.params.id)
  },
  methods: {
    handleUpload (e) {
      const files = e.target.files
      this.store.newCampaign.csv_file = files
    }
  }
}
</script>

<style scoped>
#upload-methods:hover {
  cursor: pointer;
  background-color: rgba(0, 0, 0, .075);
}
</style>
