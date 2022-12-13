<template>
  <div class="group">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <p v-if="index === 0" class="m-0">Parse <span class="fw-bold">Tag</span> when</p>
      <p v-else class="m-0">AND</p>

      <button type="button" class="btn btn-light shadow-none" @click="$emit('delete:condition', index)">
        <font-awesome-icon icon="fa-solid fa-trash" />
      </button>
      
    </div>
    
    <base-card>
      <template #body>  
        <!-- TODO: As component -->
        <div>
          <div class="d-flex justify-content-between align-items-center">
            <div class="dropdown">
              <button type="button" class="btn btn-light shadow-none" @click="showTagMenu = !showTagMenu">
                <span v-if="selectedName">{{ selectedName }}</span>
                <span v-else>Select name</span>
              </button>
  
              <div :class="{ 'd-block': showTagMenu }" class="dropdown-menu shadow p-4">
                <button type="button" class="btn btn-light btn-rounded shadow-none" @click="handleTagSelection('div')">DIV</button>
              </div>
            </div>
            <button type="button" class="btn btn-light shadow-none">OR</button>
          </div>

          <!-- Parameters -->
          <div v-if="selectedName !== null && selectedName !== ''" class="mt-2">
            <div class="my-2 d-flex justify-content-left align-items-center gap-1">
              <button v-for="(attributeParameter, i) in selectedAttributeParameters" :key="i" type="button" class="btn btn-sm btn-outline-secondary shadow-none btn-rounded">
                {{ attributeParameter.name }}<span class="fw-bold mx-1">{{ attributeParameter.operator }}</span>{{ attributeParameter.value }}
              </button>
            </div>

            <div class="dropdown">
              <button type="button" class="btn btn-light shadow-none" @click="showParametersMenu = !showParametersMenu">
                <font-awesome-icon icon="fa-solid fa-plus" class="me-2" />
                Add parameter
              </button>
              
              <!-- Attribute -->
              <div :class="{ 'd-block': showParametersMenu }" class="dropdown-menu p-3">  
                <div class="d-flex-justify-content-left gap-1">
                  <button type="button" class="btn btn-light shadow-none btn-rounded" @click="handleSelectedParameter('id')">ID</button>
                  <button type="button" class="btn btn-light shadow-none btn-rounded">Class</button>
                </div>
              </div>

              <!-- Attribute parameters -->
              <div :class="{ 'd-block': setParametersMenu }" class="dropdown-menu p-3">
                <base-input id="select-operator" />
                <base-input id="select-value" v-model="selectedAttribute.value" class="my-2" />
                <button type="button" class="btn btn-sm btn-light shadow-none" @click="setParametersMenu = false">
                  Cancel
                </button>
                <button type="button" class="btn btn-sm btn-light shadow-none" @click="setParameterAttribute">
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <div class="mt-3 border-top">
          <button type="button" class="btn btn-light shadow-none mt-3">AND</button>
        </div>
      </template>
    </base-card>
  </div>
</template>

<script>
import { inject } from 'vue'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'

export default {
  name: 'SingleCondition',
  components: {
    BaseCard,
    BaseInput
  },
  props: {
    index: {
      type: Number,
      default: 0
    }
  },
  emits: {
    'delete:condition' () {
      return true
    },
    'update:condition' () {
      return true
    }
  },
  setup () {
    inject('conditions')
  },
  data () {
    return {
      showTagMenu: false,
      showParametersMenu: false,
      setParametersMenu: false,

      selectedName: null,
      selectedAttribute: {
        name: null,
        operator: '=',
        value: null
      },
      selectedAttributeParameters: []
    }
  },
  computed: {
    finalizedCondition () {
      return {
        tag: this.selectedName,
        attrs: this.selectedAttributeParameters
      }
    }
  },
  methods: {
    handleTagSelection (tagName) {
      // Set the tag name to parse on
      // the HTML page
      this.selectedName = tagName
      this.showTagMenu = false
    },
    handleSelectedParameter (name) {
      this.selectedAttribute.name = name
      this.showParametersMenu = false
      this.setParametersMenu = true
    },
    setParameterAttribute () {
      // Set the attributes that will serve to identify certain
      // items on the HTML page
      this.selectedAttributeParameters.push(this.selectedAttribute)
      this.selectedAttribute = { name: null, operator: '=', value: null }
      this.setParametersMenu = false
      this.$emit('update:condition', [this.index, this.finalizedCondition])
    }
  }
}
</script>


<style scoped>
.dropdown {
  position: relative;
}
.dropdown-menu {
  position: absolute;
  width: 500px;
  top: 0;
  left: 0;
  height: 150px;
  z-index: 1055;
}
</style>
