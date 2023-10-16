<template>
	<div
		class="main-center col-span-3 space-y-4"
		v-if="!conversationStore.isLoading">
		<div class="bg-white border border-gray-200 rounded-lg">
			<div
				class="flex flex-col flex-grow p-4"
				v-for="message in conversationStore.messages">
				<MessageSent
					v-if="message.sender.user.id === userStore.user.id"
					:body="message.body" />
				<MessageReceived
					v-else
					:body="message.body" />
			</div>
		</div>

		<div class="bg-white border border-gray-200 rounded-lg">
			<div class="p-4">
				<textarea
					v-model="messageText"
					class="p-4 w-full bg-gray-100 rounded-lg resize-none"
					placeholder="What do you want to say?"></textarea>
			</div>

			<div class="p-4 border-t border-gray-100 flex justify-between">
				<a
					href="#"
					class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
					@click="sendMessage"
					>Post</a
				>
			</div>
		</div>
	</div>
</template>

<script>
	/**
	 * @name ConversationView
	 * @description A component that displays a conversation between two users.
	 * @component
	 *
	 * @example
	 * <ConversationView />
	 */
	import { ref } from 'vue';
	import { useConversationStore } from '@/stores/conversationStore';
	import { useUserStore } from '@/stores/user';
	import MessageReceived from './MessageReceived.vue';
	import MessageSent from './MessageSent.vue';

	export default {
		name: 'ConversationView',
		components: {
			MessageSent,
			MessageReceived,
		},
		props: {
			activeConversationId: {
				type: [String, Number],
				required: false,
			},
		},
		setup() {
			const conversationStore = useConversationStore();
			const userStore = useUserStore();
			const messageText = ref(''); // Local state for the message text

			return {
				conversationStore,
				userStore,
			};
		},
		data() {
			return {
				messageText: '',
			};
	},
		methods: {
			/**
			 * @name sendMessage
			 * @description Sends a message to the active conversation.
			 */
			sendMessage() {
				this.conversationStore.sendMessage(this.messageText);
				this.messageText = '';
				console.log('Message sent');
			},
		},
	};
</script>

<style lang="scss" scoped></style>
