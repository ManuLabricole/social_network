import { defineStore } from 'pinia'

// Define a Pinia store for managing toast notifications.
export const useToastStore = defineStore({
    id: 'toast', // Unique identifier for this store.

    state: () => ({
        ms: 0,              // Duration of the toast message.
        message: '',        // The message to display in the toast.
        classes: '',        // CSS classes for styling the toast.
        isVisible: false    // Flag to control the visibility of the toast.
    }),

    actions: {
        // Show a toast notification.
        showToast(ms, message, classes) {
            // Set the duration, message, and CSS classes for the toast.
            this.ms = parseInt(ms);
            this.message = message;
            this.classes = classes;
            this.isVisible = true;

            // Slide in the toast with a CSS class.
            setTimeout(() => {
                this.classes += ' -translate-y-28';
            }, 10);

            // Remove the sliding CSS class after the specified duration minus 500 milliseconds.
            setTimeout(() => {
                this.classes = this.classes.replace('-translate-y-28', '');
            }, this.ms - 500);

            // Hide the toast after the specified duration.
            setTimeout(() => {
                this.isVisible = false;
            }, this.ms);
        }
    }
})
