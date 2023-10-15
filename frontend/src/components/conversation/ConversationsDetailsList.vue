<template>
	<div class="main-left col-span-1">
		<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
			<div
				class="space-y-6"
				v-for="conversation in conversationStore.conversations"
				:key="conversation.id"
				@click="setActiveConversation(conversation.id)">
				<ConversationDetails
					:conversation="conversation"
					:isSelected="activeConversationId === conversation.id"
					:currentUserId="conversationStore.userId" />
			</div>
		</div>
	</div>
</template>

<script>
	import { ref } from 'vue';
	import ConversationDetails from './ConversationDetails.vue';
	import { useConversationStore } from '@/stores/conversationStore';

	export default {
		name: 'ConversationDetailsList',
		components: {
			ConversationDetails,
		},
		setup() {
			const conversationStore = useConversationStore();
			const activeConversationId = ref(null); // Define it here

			const setActiveConversation = (id) => {
				activeConversationId.value = id;
				// Emit the event here if needed
			};

			return {
				conversationStore,
				activeConversationId, // Make it available to the template
				setActiveConversation, // Make the method available to the template
			};
		},
		mounted() {
			this.conversationStore.fetchConversations();
		},
		methods: {
			setActiveConversation(id) {
				this.activeConversationId = id;
				this.$emit('active-conversation-changed', id);
			},
		},
	};
</script>

<style scoped></style>
