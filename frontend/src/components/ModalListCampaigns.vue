<template>
  <base-modal :show="show" scrollable @close="$emit('close')">
    <template #default>
      <div class="row">
        <div class="col-3">
          <base-nav-pills :items="navItems" />
        </div>

        <div class="col-9">
          <div class="row">
            <div v-for="campaign in store.availableCampaigns" :key="campaign.id" class="col-4">
              <router-link :to="{ name: 'campaign_setup_view', params: { id: campaign.id } }">
                <base-card class="my-1" :title="campaign.name">
                  <template #body>
                    <div class="fw-light">
                      {{ campaign.description }}
                    </div>
                  </template>
                </base-card>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </template>
  </base-modal>
</template>

<script>
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
      navItems: [
        {
          name: 'User selected'
        },
        {
          name: 'Linkedin'
        }
      ]
    }
  }
}
</script>
