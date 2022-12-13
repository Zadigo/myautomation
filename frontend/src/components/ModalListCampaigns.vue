<template>
  <base-modal :show="show" scrollable @close="$emit('close')">
    <template #default>
      <div v-if="preview" class="container">
        <div class="row">
          <div class="col-12">
            <div class="d-flex justify-content-between align-items-center">
              <button type="button" class="btn btn-light mb-3 shadow-none" @click="preview = false">
                <font-awesome-icon icon="fa-solid fa-arrow-left" class="me-2" />
                Back to templates
              </button>
            </div>

            <div class="row">
              <div class="col-8">
                <!-- TODO: Be careful. This might raise an error when previewedCampaign is empty -->
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
                Provident rem autem animi veniam repudiandae aspernatur error debitis 
                voluptates veritatis, assumenda est? Eum laboriosam nobis assumenda nam 
                debitis magnam, aspernatur sed!
              </div>

              <div class="col-4">
                
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="row">
        <div class="col-3 text-center">
          <base-nav-pills :items="navItems" is-pills @click:nav-pill="(value) => { filteredBy = value[1].name }" />
        </div>

        <div class="col-9">
          <div class="row">
            <div v-for="campaignTemplate in filteredCampaignTemplates" :key="campaignTemplate.id" class="col-4">
              <base-card class="my-1" :title="campaignTemplate.name">
                <template #body>
                  <div v-if="campaignTemplate.premium" class="badge badge-pill badge-warning my-3">
                    <font-awesome-icon icon="fa-solid fa-star" class="me-2" /> Premium
                  </div>
                  
                  <p class="fw-light py-2">
                    {{ campaignTemplate.description }}
                  </p>

                  <div class="btn-group">
                    <button type="button" class="btn btn-primary" @click="handlePreview(campaignTemplate)">
                      <!-- <font-awesome-icon icon="fa-solid fa-eye" class="me-2" /> -->
                      Preview
                    </button>
                    <router-link :to="{ name: 'campaign_setup_view', params: { id: campaignTemplate.id } }" class="btn btn-primary">
                      Select
                    </router-link>
                  </div>
                </template>
              </base-card>
            </div>
          </div>
        </div>
      </div>
    </template>
  </base-modal>
</template>

<script>
import _ from 'lodash'
import { useCampaigns } from '@/store/campaigns'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseModal from '@/layouts/bootstrap/BaseModal.vue'
import BaseNavPills from '@/layouts/bootstrap/BaseNavPills.vue'

export default {
  name: 'ModalListCampaigns',
  components: {
    BaseCard,
    BaseModal,
    BaseNavPills
  },
  props: {
    show: {
      type: Boolean
    }
  },
  emits: {
    close () {
      return true
    }
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  data () {
    return {
      filteredBy: 'All',
      previewedCampaign: {},
      preview: false,
      navItems: [
        {
          name: 'All'
        },
        {
          name: 'User selected'
        },
        {
          name: 'Linkedin'
        }
      ]
    }
  },
  computed: {
    campaignTemplates () {
      return this.store.campaignTemplates
    },
    filteredCampaignTemplates () {
      if (this.filteredBy === 'All') {
        return this.campaignTemplates
      } else {
        return _.filter(this.campaignTemplates, (campaign) => {
          if (this.filteredBy === 'User selected') {
            return campaign.free_form
          } else if (this.filteredBy === 'Linkedin') {
            return campaign.social_media
          }
          return []
        })
      }
    }
  },
  methods: {
    handlePreview (campaign) {
      this.previewedCampaign = campaign
      this.preview = true
    }
  }
}
</script>
