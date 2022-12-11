<template>
  <select v-model="value" class="form-select" @change="emitValue($event)">
    <option v-for="(item, i) in items" :key="i">
      {{ item }}
    </option>
  </select>
</template>

<script>
export default {
  name: 'BaseSelect',
  props: {
    items: {
      type: Array
    },
    modelValue: {
      type: String
    }
  },
  emits: {
    'update:modelValue' () {
      return true
    }
  },
  computed: {
    value: {
      get () {
        return this.modelValue
      },
      set (value) {
        return this.$emit('update:modelValue', value)
      }
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
.form-select option {
  min-height: 3em;
  padding: .5rem 1rem;
}
</style>
