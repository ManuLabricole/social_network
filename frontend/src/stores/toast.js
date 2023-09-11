import { defineStore } from 'pinia'

export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    }),

    actions: {
        showToast(ms, message, classes) {
            console.log('toast show ')
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true

            setTimeout(() => {
                console.log('toast translate in ')
                this.classes += ' -translate-y-28'
            }, 10)

            setTimeout(() => {
                console.log('toast translate out ')
                this.classes = this.classes.replace('-translate-y-28', '')
            }, this.ms - 500)

            setTimeout(() => {
                console.log('toast hide ')
                this.isVisible = false
            }, this.ms)
        }
    }
})
