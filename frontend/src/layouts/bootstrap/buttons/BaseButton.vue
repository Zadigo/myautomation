<template>
  <router-link v-if="to" :id="computedId" :to="to" :class="buttonClasses" v-bind="buttonAttrs">
    <slot></slot>
  </router-link>
  
  <button v-else :id="computedId" :class="buttonClasses" v-bind="buttonAttrs" type="button">
    <slot></slot>
  </button>
</template>

<script>
import { ref } from 'vue'
import { useUtilities } from '../composables'

export default {
  name: 'BaseButton',
  props: {
    id: {
      type: String
    },
    color: {
      type: String,
      default: 'primary'
    },
    disabled: {
      type: Boolean
    },
    placeholder: {
      type: Boolean
    },
    to: {
      type: [String, Object]
    }
  },
  setup () {
    const target = ref(null)
    const { generateId } = useUtilities()
    return {
      target,
      generateId
    }
  },
  computed: {
    buttonClasses () {
      return [
        'btn',
        {
          [`btn-${this.color}`]: true,
          'disabled': this.placeholder || this.disabled,
          'placeholder': this.placeholder 
        }
      ]
    },
    buttonAttrs () {
      return {

      }
    },
    computedId () {
      return this.id || this.generateId('btn')
    }
  }
}
</script>
