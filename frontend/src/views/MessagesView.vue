<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<div class="main-left col-span-1">
			<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
				<div class="space-y-4">
					<div class="flex items-center justify-between">
						<div class="flex items-center space-x-2">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-[40px] rounded-full" />

							<p class="text-xs"><strong>Code With Stein</strong></p>
						</div>

						<span class="text-xs text-gray-500">18 minutes ago</span>
					</div>

					<div class="flex items-center justify-between">
						<div class="flex items-center space-x-2">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-[40px] rounded-full" />

							<p class="text-xs"><strong>Code With Stein</strong></p>
						</div>

						<span class="text-xs text-gray-500">18 minutes ago</span>
					</div>

					<div class="flex items-center justify-between">
						<div class="flex items-center space-x-2">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-[40px] rounded-full" />

							<p class="text-xs"><strong>Code With Stein</strong></p>
						</div>

						<span class="text-xs text-gray-500">18 minutes ago</span>
					</div>
				</div>
			</div>
		</div>

		<div class="main-center col-span-3 space-y-4">
			<div class="bg-white border border-gray-200 rounded-lg">
				<div class="flex flex-col flex-grow p-4">
					<div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
						<div
							class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg max-w-[100%] whitespace-normal">
							<p class="text-sm break-words">HelloHellolloHelloHelloHello !</p>
						</div>
						<span
							class="text-xs text-gray-500 leading-none absolute bottom-0 left-0 ml-3 mb-2"
							>2 min ago</span
						>

						<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-10 h-10 rounded-full" />
						</div>
					</div>
					<div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
						<div
							class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg max-w-[100%] whitespace-normal">
							<p class="text-sm break-words">Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime aperiam alias molestiae , perspi !</p>
						</div>
						<span
							class="text-xs text-gray-500 leading-none absolute bottom-0 left-0 ml-3 mb-2"
							>2 min ago</span
						>

						<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-10 h-10 rounded-full" />
						</div>
					</div>
					<div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
						<div
							class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg max-w-[100%] whitespace-normal">
							<p class="text-sm break-words">
								Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim
								quidem temporibus molestiae, quibusdam, veniam recusandae
								ratione corporis architecto placeat expedita et dolor, vel
								magnam labore est consectetur eius consequuntur voluptate!
							</p>
						</div>
						<span
							class="text-xs text-gray-500 leading-none absolute bottom-0 left-0 ml-3 mb-2"
							>2 min ago</span
						>

						<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-10 h-10 rounded-full" />
						</div>
					</div>
					<div class="flex w-full mt-2 space-x-3 max-w-md">
						<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-[40px] rounded-full" />
						</div>
						<div>
							<div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
								<p class="text-sm">
									Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
									do eiusmod tempor incididunt ut labore et dolore magna aliqua.
								</p>
							</div>
							<span class="text-xs text-gray-500 leading-none">2 min ago</span>
						</div>
					</div>
					<div class="flex w-full mt-2 space-x-3 max-w-md">
						<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
							<img
								src="https://i.pravatar.cc/300?img=70"
								class="w-[40px] rounded-full" />
						</div>
						<div>
							<div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
								<p class="text-sm">
									Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
									do eiusmod tempor incididunt ut labore et dolore magna aliqua.
								</p>
							</div>
							<span class="text-xs text-gray-500 leading-none">2 min ago</span>
						</div>
					</div>
				</div>
			</div>

			<div class="bg-white border border-gray-200 rounded-lg">
				<div class="p-4">
					<textarea
						class="p-4 w-full bg-gray-100 rounded-lg resize-none"
						placeholder="What do you want to say?"></textarea>
				</div>

				<div class="p-4 border-t border-gray-100 flex justify-between">
					<a
						href="#"
						class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
						>Post</a
					>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'HomeView',
		components: {},
		setup() {
			return {};
		},
	};
</script>

<style lang="postcss" scoped></style>
