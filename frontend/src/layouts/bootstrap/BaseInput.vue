<template>
  <input :id="id" :value="modelValue" :type="inputType" :name="id" :class="inputClasses" class="form-control" @input="emitValue($event)">
</template>

<script>
import { inject } from 'vue'

export default {
  name: 'BaseInput',
  props: {
    id: {
      type: String,
      required: true
    },
    inputType: {
      type: String,
      default: 'text'
    },
    modelValue: {
      type: [String, Number, Boolean]
    }
  },
  emits: {
    'update:modelValue' () {
      return true
    }
  },
  setup () {
    const darkMode = inject('darkMode', false)
    return {
      darkMode
    }
  },
  computed: {
    inputClasses () {
      return [
        {
          'bg-transparent text-light': this.darkMode
        }
      ]
    }
  },
  methods: {
    emitValue (e) {
      let value = e.target.value
      if (this.inputType === 'number') {
        value = value * 1
      }
      this.$emit('update:modelValue', value)
    }
  }
}
</script>

<style scoped>
.form-control {
  padding-inline-start: 16px;
  padding-inline-end: 16px;
  padding-top: 8px;
  padding-bottom: 8px;
}
</style>
