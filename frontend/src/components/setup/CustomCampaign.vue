<doc>
  When the user creates a campaign for a random
  website that is not a social media type
</doc>

<template>
  <section>
    <div class="container">
      <div class="row">
        <div class="col-sm-12 col-md-6">
          <!-- Parsing options -->
          <base-card title="Choose the sections of the page to parse">
            <template #body>
              <!-- <label for="select-section" class="fw-bold">Choose the section of the page to parse</label> -->
              <base-input id="select-section" v-model="store.newCampaign.section_to_parse" :disabled="store.newCampaign.parse_all_tables || store.newCampaign.parse_all_text" placeholder="e.g. div#section" />

              <button type="button" class="btn btn-info mt-2 disabled" @click="showLogicalMap = !showLogicalMap">
                <font-awesome-icon icon="fa-solid fa-list-check" class="me-2" />
                Use logical map
              </button>

              <div class="mt-4">
                <p v-if="store.newCampaign.parse_all_text" class="alert alert-info my-2">
                  <font-awesome-icon icon="fa-solid fa-circle-info" class="me-2" />
                  Choosing this option might return some incoherent data in your dataset. For better results,
                  indicate a section of the page that you would like to parse
                </p>

                <base-list-group>
                  <base-list-group-item class="p-4">
                    <base-checkbox id="select-parse-all-tables" v-model="store.newCampaign.parse_all_tables" :disabled="store.newCampaign.parse_all_text" label="Parse all the tables on the page" is-switch />
                  </base-list-group-item>

                  <base-list-group-item class="p-4">
                    <base-checkbox id="select-parse-all-text" v-model="store.newCampaign.parse_all_text" :disabled="store.newCampaign.parse_all_tables" label="Parse all the text on the page" is-switch />
                  </base-list-group-item>
                </base-list-group>
                
                <h5 class="mt-4 mb-0">Choose which data to return</h5>
                <div class="alert alert-info my-2">
                  <font-awesome-icon icon="fa-solid fa-info-circle" class="me-2" />
                  You can also choose to get only the items on the page that match
                  one of the following conditions below
                </div>
                
                <base-list-group-checkbox id="scrap-choices" :items="scrapChoices" @list-group-selection="handleSelection" />
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

        <!-- Logical conditions -->
        <div v-if="showLogicalMap" class="col-sm-12 col-md-6">
          <conditions-group />
        </div>

        <!-- Static logical conditions -->
        <div v-else class="col-sm-12 col-md-6" style="position:relative;">
          <div class="logical-map" style="position: sticky;top: 0;left: 0;">
            <base-card class="text-center">
              <template #body>
                <div class="fs-4 fw-bold">PARSE <span class="text-info">{{ quantifier }}</span> {{ elementType }}</div> 
              </template>
            </base-card>
            
            <div v-if="store.newCampaign.data_constraint.length > 0" class="operation">
              <div class="line"></div>
              <h3 class="text-light bg-dark p-2 rounded">AND</h3>
              <div class="line"></div>
            </div>
  
            <base-card v-if="store.newCampaign.data_constraint.length" class="text-center">
              <template #body>
                <div class="fs-4 fw-bold text-info">ONLY</div>
                <div class="fs-4 fw-bold">{{ store.newCampaign.data_constraint.join(', ') }}</div>
              </template>
            </base-card>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import { useUtilities } from '@/composables/utils'
import { useCampaigns } from '@/store/campaigns'
import { useNavigation } from '@/composables/navigation'
import { getCurrentInstance } from 'vue'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'
import ConditionsGroup from '../conditions/ConditionsGroup.vue'
import BaseListGroup from '@/layouts/bootstrap/listgroup/BaseListGroup.vue'
import BaseListGroupCheckbox from '@/layouts/bootstrap/listgroups/BaseListGroupCheckbox.vue'
import BaseListGroupItem from '@/layouts/bootstrap/listgroup/BaseListGroupItem.vue'

export default {
  name: 'CustomCampaign',
  components: {
    BaseCard,
    BaseCheckbox,
    BaseInput,
    BaseListGroup,
    BaseListGroupCheckbox,
    BaseListGroupItem,
    ConditionsGroup
  },
  setup () {
    const { listManager  } = useUtilities()
    const app = getCurrentInstance()
    const { goToNext, goToPrevious } = useNavigation(app)
    const store = useCampaigns()
    return {
      store,
      goToPrevious,
      goToNext,
      listManager
    }
  },
  data () {
    return {
      showLogicalMap: false,
      scrapChoices: [
        {
          name: 'Emails',
          subtitle: 'Get emails'
        },
        {
          name: 'Telephone',
          subtitle: 'Get telephone numbers'
        },
        {
          name: 'Images',
          subtitle: 'Get all images'
        },
        {
          name: 'Links',
          subtitle: 'Get all links'
        }
      ]
    }
  },
  computed: {
    quantifier () {
      if (this.store.newCampaign.parse_all_text || this.store.newCampaign.parse_all_tables) {
        return 'ALL'
      } else {
        return this.store.newCampaign.section_to_parse
      }
    },
    elementType () {
      if (this.store.newCampaign.parse_all_text) {
        return 'TEXT'
      } else if (this.store.newCampaign.parse_all_tables) {
        return 'TABLES'
      } else {
        return null
      }
    }
  },
  methods: {
    handleSelection (values) {
      this.store.newCampaign.data_constraint = _.map(values, (value) => {
        return value.name
      })
    }
  },
}
</script>

<style scoped>
/* .logical-map .card {
  margin-bottom: 3rem;
} */

.line {
  /* margin: 0 auto; */
  margin-top: 1rem;
  margin-bottom: 1rem;
  background-color: rgba(38, 38, 38, 1);
  width: 5px;
  height: 30px;
}
.operation {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
