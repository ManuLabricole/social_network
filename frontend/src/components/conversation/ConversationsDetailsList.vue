<template>
	<div class="main-left col-span-1">
		<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
			<div class="space-y-4">
				<ConversationDetails />
				<ConversationDetails />
				<ConversationDetails />
				<ConversationDetails />
			</div>
		</div>
	</div>
</template>

<script>
	import ConversationDetails from './ConversationDetails.vue';
	import { useConversationStore } from '@/stores/conversationStore';
	import { onMounted } from 'vue';

	export default {
		name: 'ConversationDetailsList',
		components: {
			ConversationDetails,
		},
		setup() {
			const conversationStore = useConversationStore();
			return {
				conversationStore,
			};
		},
		mounted() {
			onMounted(() => {
				this.conversationStore.fetchConversations();
				console.log('mounted');
			});
		},
	};
</script>

<style scoped></style>
