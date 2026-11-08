from universe.audio.pilot_line import PilotLine as L
from universe.audio import parse_rule as R
from universe.audio.base_pilot import EnglishBaseIdentifiedVoice, EnglishCommodityVoice
from universe.audio.static import dispatcher as dispatcher_static

from text.strings import MultiString as MS


class EnglishStationDispatcher(EnglishBaseIdentifiedVoice):
    DENOISE = False
    TRIM_LEAD = True
    VOICE_DATA = dispatcher_static.VOICE_DATA
    MVOICE_AUDIO_PROP = ''
    MVOICE_MISSION_PROP = ''
    LINES = [
        L('mod_refer_base_liner-','liner', R.RuleBaseNoProcess),
        L('mod_refer_base_roid_miner-', 'Roid Miner', R.RuleBaseNoProcess),
        L('mod_refer_base_gas_miner-', 'Gas Miner', R.RuleBaseNoProcess),
        L('mod_refer_base_solar_plant-', 'Solar Plant', R.RuleBaseNoProcess),
        L('mod_refer_base_research_base-', 'Research Base', R.RuleBaseNoProcess),
        L('mod_refer_base_battleship-', 'Battleship', R.RuleBaseNoProcess),
        L('mod_refer_base_freeport-', 'Freeport', R.RuleBaseNoProcess),
        L('mod_refer_base_prison-', 'Prison', R.RuleBaseNoProcess),
        L('mod_refer_base_outpost-', 'Outpost', R.RuleBaseNoProcess),
        L('mod_refer_base_research-', 'Research', R.RuleBaseNoProcess),
        L('mod_refer_base_shipyard-', 'Shipyard', R.RuleBaseNoProcess),
        L('mod_refer_base_factory-', 'Factory', R.RuleBaseNoProcess),
        L('mod_refer_base_station-', 'Station', R.RuleBaseNoProcess),
        L('mod_refer_base_border-', 'Border Station', R.RuleBaseNoProcess),

        L('gcs_refer_shiparch_borf', 'Dromader', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_borhf', 'Stiletto', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_borvhf', 'Sabre', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_borlf', 'Dagger', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Breb', 'Bretonia battleship', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Bred', 'Bretonia destroyer', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Bref', 'Clydesdale', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Breg', 'Bretonia gunboat', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Brehf', 'Crusader', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Brelf', 'Cavalier', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_ctransport', 'transport train', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_hlifter', 'heavy lifter', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_htransport', 'heavy transport', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Kusb', 'Kusari battleship', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Kusd', 'Kusari destroyer', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Kusf', 'Drone', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Kusg', 'Kusari gunboat', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Kushf', 'Dragon', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Kuslf', 'Drake', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Libb', 'Liberty battleship', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Libc', 'Liberty cruiser', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Libf', 'Rhino', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Libhf', 'Defender', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Liblf', 'Patriot', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_ordhf', 'Anubis', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_pirf', 'Mule', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_pirhf', 'Wolfhound', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_pirlf', 'Bloodhound', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_repair', 'repair ship', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Rheb', 'Rheinland battleship', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Rhed', 'Rheinland cruiser', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Rhef', 'Humpback', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Rheg', 'Rheinland gunboat', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Rhehf', 'Valkyrie', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_Rhelf', 'Banshee', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_starblazer', 'Starblazer', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_starflier', 'Starflier', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_startracker', 'Startracker', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_gf4', 'Hawk', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_gf5', 'Falcon', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_gf6', 'Eagle', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_colf', 'Legionnaire', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_cohf', 'Centurion', R.RuleAskNoProcess),
        L('gcs_refer_shiparch_covhf', 'Titan', R.RuleAskNoProcess),
    ]

    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class EngMaleDispatcher(EnglishCommodityVoice, EnglishStationDispatcher):
    STEOS_ID = 294  # lebedev, stalker
    FOLDER = 'dispatcher_en01'
    ATTENUATION = -4
    def get_lines(self):
        lines = list(super().get_lines())
        lines.extend([
            L('tc_board_01-', 'Hello, Mr. Trent. Your locomotive is waiting by the docking fixture. Dock with it to begin your shift.', R.RuleDefaultNoProcess),
            L('tc_board_02-', 'Freight dispatch here. Your locomotive is ready. Follow the marker and dock with it to take over.', R.RuleDefaultNoProcess),
            L('tc_board_03-', 'Welcome aboard, Trent. First, dock with the locomotive waiting beside the docking fixture.', R.RuleDefaultNoProcess),
            L('tc_board_04-', 'Mr. Trent, your locomotive is marked on the navigation display. Approach it and request docking.', R.RuleDefaultNoProcess),
            L('tc_board_05-', 'Dispatch to Trent. The locomotive is ready for you. Dock with it, and I will send you your first order.', R.RuleDefaultNoProcess),
            L('tc_board_06-', 'Your shift is confirmed. Head for the marked locomotive and dock with it to take the controls.', R.RuleDefaultNoProcess),
            L('tc_board_07-', 'Good to hear from you, Mr. Trent. The locomotive is waiting at the fixture. Dock with it when you are ready.', R.RuleDefaultNoProcess),
            L('tc_board_08-', 'We have a locomotive ready for you, Trent. Its position is marked. Dock with it to start work.', R.RuleDefaultNoProcess),
            L('tc_board_09-', 'Freight control calling. Take over the locomotive at the marked position by docking with it.', R.RuleDefaultNoProcess),
            L('tc_board_10-', 'Mr. Trent, everything is ready for your shift. Dock with the locomotive beside the docking fixture.', R.RuleDefaultNoProcess),
            L('tc_order_01+', 'We have an order for', R.RuleDefaultNoProcess),
            L('tc_order_02+', 'Mr. Trent, your assignment is a shipment of', R.RuleDefaultNoProcess),
            L('tc_order_03+', 'Dispatch has a delivery order for', R.RuleDefaultNoProcess),
            L('tc_order_04+', 'Your cargo for this run is', R.RuleDefaultNoProcess),
            L('tc_order_05+', 'Trent, we need you to transport', R.RuleDefaultNoProcess),
            L('tc_order_06+', 'The shipment assigned to you contains', R.RuleDefaultNoProcess),
            L('tc_order_07+', 'Here are your instructions. You will be carrying', R.RuleDefaultNoProcess),
            L('tc_order_08+', 'I have a freight order for you. The cargo is', R.RuleDefaultNoProcess),
            L('tc_order_09+', 'Mr. Trent, we have a shipment ready. You will be delivering', R.RuleDefaultNoProcess),
            L('tc_order_10+', 'This run is a delivery of', R.RuleDefaultNoProcess),
            L('tc_destination_01+', 'for delivery to', R.RuleDefaultNoProcess),
            L('tc_destination_02+', 'bound for', R.RuleDefaultNoProcess),
            L('tc_destination_03+', 'to be delivered to', R.RuleDefaultNoProcess),
            L('tc_destination_04+', 'consigned to', R.RuleDefaultNoProcess),
            L('tc_destination_05+', 'for transport to', R.RuleDefaultNoProcess),
            L('tc_destination_06+', 'destined for', R.RuleDefaultNoProcess),
            L('tc_destination_07+', 'for shipment to', R.RuleDefaultNoProcess),
            L('tc_destination_08+', 'with delivery requested at', R.RuleDefaultNoProcess),
            L('tc_destination_09+', 'with the delivery point at', R.RuleDefaultNoProcess),
            L('tc_destination_10+', 'with the receiving depot at', R.RuleDefaultNoProcess),
            L('tc_collect_01-', "Collect the cargo at the marked waypoint. Bring the rear of your locomotive close to the wagons' coupling point, then use the coupling manoeuvre to attach the train.", R.RuleDefaultNoProcess),
            L('tc_collect_02-', 'The loaded wagons are waiting at the marked waypoint. Approach their coupling point with the rear of your locomotive and use the coupling manoeuvre to connect them.', R.RuleDefaultNoProcess),
            L('tc_collect_03-', "Pick up the shipment at the indicated waypoint. Line up the rear of your locomotive with the wagons' coupling point, move close, and activate the coupling manoeuvre.", R.RuleDefaultNoProcess),
            L('tc_collect_04-', 'Your wagons are marked on the navigation display. Back the locomotive towards their coupling point, then use the coupling manoeuvre to attach them.', R.RuleDefaultNoProcess),
            L('tc_collect_05-', 'Go to the marked pickup point. Bring the back of your locomotive up to the coupling point on the wagons and engage the coupling manoeuvre.', R.RuleDefaultNoProcess),
            L('tc_collect_06-', 'The cargo is ready at the waypoint. Approach the wagons stern first, line up with their coupling point, and use the coupling manoeuvre to secure the train.', R.RuleDefaultNoProcess),
            L('tc_collect_07-', 'Follow the waypoint to your loaded wagons. Move the rear of the locomotive close to their coupling point, then activate the coupling manoeuvre.', R.RuleDefaultNoProcess),
            L('tc_collect_08-', 'Collect the assigned wagons at the marked location. Back towards their coupling point and use the coupling manoeuvre once your locomotive is close.', R.RuleDefaultNoProcess),
            L('tc_collect_09-', "The pickup location is marked. Align the rear of your locomotive with the wagons' coupling point, approach carefully, and engage the coupling manoeuvre.", R.RuleDefaultNoProcess),
            L('tc_collect_10-', "Proceed to the pickup waypoint. Bring your locomotive into position with its rear near the wagons' coupling point, then use the coupling manoeuvre to attach the train.", R.RuleDefaultNoProcess),
            L('tc_depart_01+', 'Coupling confirmed. Deliver this shipment to', R.RuleDefaultNoProcess),
            L('tc_depart_02+', 'The wagons are attached, Mr. Trent. Take the cargo to', R.RuleDefaultNoProcess),
            L('tc_depart_03+', 'Your train is connected. Proceed with the delivery to', R.RuleDefaultNoProcess),
            L('tc_depart_04+', 'Cargo secured. Your delivery point is at', R.RuleDefaultNoProcess),
            L('tc_depart_05+', 'You are ready to depart, Trent. Deliver the cargo to', R.RuleDefaultNoProcess),
            L('tc_depart_06+', 'The coupling is secure. Head for the receiving depot at', R.RuleDefaultNoProcess),
            L('tc_depart_07+', 'Train connection confirmed. Transport the shipment to', R.RuleDefaultNoProcess),
            L('tc_depart_08+', 'All set, Mr. Trent. Follow the route and deliver the shipment to', R.RuleDefaultNoProcess),
            L('tc_depart_09+', 'The wagons are connected. Take this load to', R.RuleDefaultNoProcess),
            L('tc_depart_10+', 'Dispatch confirms the coupling. Your destination is', R.RuleDefaultNoProcess),
            L('tc_arrival_01-', 'You have reached the delivery area. Bring the wagons to a stop at the marker, then uncouple them.', R.RuleDefaultNoProcess),
            L('tc_arrival_02-', 'This is the receiving point, Trent. Stop the loaded wagons inside the marked area and release the coupling.', R.RuleDefaultNoProcess),
            L('tc_arrival_03-', 'You are at the depot. Position the wagons at the delivery marker, come to a halt, and uncouple.', R.RuleDefaultNoProcess),
            L('tc_arrival_04-', 'The delivery area is ahead. Bring the train to a stop with the wagons at the marker, then detach them.', R.RuleDefaultNoProcess),
            L('tc_arrival_05-', 'Mr. Trent, leave the loaded wagons in the marked delivery area. Stop first, then uncouple the train.', R.RuleDefaultNoProcess),
            L('tc_arrival_06-', 'Your receiving point is marked. Move the wagons into position, bring them to a halt, and release the coupling.', R.RuleDefaultNoProcess),
            L('tc_arrival_07-', 'You are close enough to make the delivery. Stop the wagons at the marker and uncouple them.', R.RuleDefaultNoProcess),
            L('tc_arrival_08-', 'Dispatch to Trent. Park the loaded wagons within the delivery area, then uncouple once they have stopped.', R.RuleDefaultNoProcess),
            L('tc_arrival_09-', 'This is where the shipment is due. Leave the wagons stationary at the marker and detach the locomotive.', R.RuleDefaultNoProcess),
            L('tc_arrival_10-', 'Approach the delivery marker carefully. Stop the loaded wagons inside the marked area, then release them.', R.RuleDefaultNoProcess),
            L('tc_paid_01-', 'Delivery confirmed. Your payment has been transferred.', R.RuleDefaultNoProcess),
            L('tc_paid_02-', 'The shipment is received, Mr. Trent. Payment is in your account.', R.RuleDefaultNoProcess),
            L('tc_paid_03-', 'Cargo accepted. You have been paid for this delivery.', R.RuleDefaultNoProcess),
            L('tc_paid_04-', 'That delivery is complete, Trent. Your payment has been credited.', R.RuleDefaultNoProcess),
            L('tc_paid_05-', 'The wagons have been received. Payment for the run has been transferred.', R.RuleDefaultNoProcess),
            L('tc_paid_06-', 'Dispatch confirms receipt of the shipment. Your account has been credited.', R.RuleDefaultNoProcess),
            L('tc_paid_07-', 'The delivery is recorded, Mr. Trent. Your payment is through.', R.RuleDefaultNoProcess),
            L('tc_paid_08-', 'Shipment accepted and payment transferred. Thank you, Trent.', R.RuleDefaultNoProcess),
            L('tc_paid_09-', 'The receiving depot has the cargo. You have been paid.', R.RuleDefaultNoProcess),
            L('tc_paid_10-', 'This order is complete. Payment has been sent to your account.', R.RuleDefaultNoProcess),
            L('tc_continue_01-', 'Ready for another delivery, Mr. Trent?', R.RuleDefaultNoProcess),
            L('tc_continue_02-', 'Would you like to take another order?', R.RuleDefaultNoProcess),
            L('tc_continue_03-', 'Shall I assign you another run, Trent?', R.RuleDefaultNoProcess),
            L('tc_continue_04-', 'Do you want to continue your shift?', R.RuleDefaultNoProcess),
            L('tc_continue_05-', 'Are you available for another shipment?', R.RuleDefaultNoProcess),
            L('tc_continue_06-', 'Mr. Trent, would you like another delivery assignment?', R.RuleDefaultNoProcess),
            L('tc_continue_07-', 'Shall we keep you on freight duty for another run?', R.RuleDefaultNoProcess),
            L('tc_continue_08-', 'Would you like to stay on for another order, Trent?', R.RuleDefaultNoProcess),
            L('tc_continue_09-', 'Are you ready to take on another delivery?', R.RuleDefaultNoProcess),
            L('tc_continue_10-', 'Let me know, Mr. Trent. Shall we continue?', R.RuleDefaultNoProcess),
            L('tc_recover_01-', 'Trent, your cargo has detached. Return to the marked wagons and couple to them again.', R.RuleDefaultNoProcess),
            L('tc_recover_02-', 'The train is no longer connected, Mr. Trent. Your wagons are marked. Go back and recover them.', R.RuleDefaultNoProcess),
            L('tc_recover_03-', 'Dispatch to Trent. You have lost the coupling. Return to the cargo marker and reconnect the train.', R.RuleDefaultNoProcess),
            L('tc_recover_04-', 'Your wagons have come loose. Follow the marker back to them and use the coupling manoeuvre again.', R.RuleDefaultNoProcess),
            L('tc_recover_05-', 'Cargo connection lost. Bring the rear of your locomotive back to the marked wagons and recouple.', R.RuleDefaultNoProcess),
            L('tc_recover_06-', 'Mr. Trent, the shipment is still behind you. Return to the marked wagons and restore the coupling.', R.RuleDefaultNoProcess),
            L('tc_recover_07-', 'The cargo is detached, Trent. I have marked its position. Go back and couple to the wagons.', R.RuleDefaultNoProcess),
            L('tc_recover_08-', 'You are travelling without the shipment. Return to the cargo waypoint and reconnect your train.', R.RuleDefaultNoProcess),
            L('tc_recover_09-', 'The coupling has been released away from the delivery point. Recover the marked wagons before continuing.', R.RuleDefaultNoProcess),
            L('tc_recover_10-', 'Dispatch confirms a detached load. Find your wagons at the marker, approach their coupling point stern first, and recouple.', R.RuleDefaultNoProcess),
            L('tc_park_01+', 'Understood. To finish your shift, park the locomotive at the marked docking fixture serving', R.RuleDefaultNoProcess),
            L('tc_park_02+', 'We will close your shift, Trent. Return the locomotive to the marked parking position at', R.RuleDefaultNoProcess),
            L('tc_park_03+', 'No further orders. Park the locomotive beside the marked docking fixture at', R.RuleDefaultNoProcess),
            L('tc_park_04+', 'All right, Mr. Trent. Bring the locomotive to the marked parking berth at', R.RuleDefaultNoProcess),
            L('tc_park_05+', 'Your shift is ending. Follow the route and park the locomotive at the docking fixture serving', R.RuleDefaultNoProcess),
            L('tc_park_06+', 'Dispatch confirms the end of your shift. Return the locomotive to the marked berth at', R.RuleDefaultNoProcess),
            L('tc_park_07+', 'Time to return the locomotive, Trent. The parking position is by the docking fixture at', R.RuleDefaultNoProcess),
            L('tc_park_08+', 'We are ready for the handover. Park your locomotive at the marked fixture serving', R.RuleDefaultNoProcess),
            L('tc_park_09+', 'Mr. Trent, your return route is set. Park the locomotive in the marked position at', R.RuleDefaultNoProcess),
            L('tc_park_10+', 'That will be all for this shift. Bring the locomotive to the marked docking fixture at', R.RuleDefaultNoProcess),
            L('tc_done_01-', 'The locomotive is parked, and you are back aboard your own ship. Thank you for your work, Mr. Trent.', R.RuleDefaultNoProcess),
            L('tc_done_02-', 'Handover complete, Trent. Your shift is finished. Safe flying.', R.RuleDefaultNoProcess),
            L('tc_done_03-', 'Your own ship is clear of the locomotive. The shift is closed. Thank you, Mr. Trent.', R.RuleDefaultNoProcess),
            L('tc_done_04-', 'The locomotive has been returned. You are free to go, Trent. Dispatch out.', R.RuleDefaultNoProcess),
            L('tc_done_05-', 'Your shift is complete, Mr. Trent. Thank you for the deliveries. Safe travels.', R.RuleDefaultNoProcess),
            L('tc_done_06-', 'We have the locomotive, and you have your ship back. Thank you for your work.', R.RuleDefaultNoProcess),
            L('tc_done_07-', 'Handover confirmed. Your freight duty is complete, Trent. Until next time.', R.RuleDefaultNoProcess),
            L('tc_done_08-', 'You are back on your own ship, Mr. Trent. The shift is closed. Have a good flight.', R.RuleDefaultNoProcess),
            L('tc_done_09-', 'The locomotive is secured. Thank you for your service today, Trent. Dispatch out.', R.RuleDefaultNoProcess),
            L('tc_done_10-', 'That completes the handover. You are free to depart in your own ship. Until the next run, Mr. Trent.', R.RuleDefaultNoProcess),
        ])
        # Empty locomotive transfer to the next pickup base.
        lines.extend([
            L('tc_reposition_01+', 'There is no suitable outbound load here, Mr. Trent. Your next train is waiting at', R.RuleDefaultNoProcess),
            L('tc_reposition_02+', 'Nothing here matches the next delivery. Take the locomotive to collect a new train at', R.RuleDefaultNoProcess),
            L('tc_reposition_03+', 'Dispatch has found your next load at another depot. Head for', R.RuleDefaultNoProcess),
            L('tc_reposition_04+', 'This depot has no suitable shipment for your next run. The pickup point is at', R.RuleDefaultNoProcess),
            L('tc_reposition_05+', 'Your next assignment starts elsewhere, Trent. Go to the loading point at', R.RuleDefaultNoProcess),
            L('tc_reposition_06+', 'We need to move the locomotive before loading again. Your next train is at', R.RuleDefaultNoProcess),
            L('tc_reposition_07+', 'There is no matching freight order at this depot. I have arranged a pickup at', R.RuleDefaultNoProcess),
            L('tc_reposition_08+', 'The next loaded train is at a different base. Proceed to', R.RuleDefaultNoProcess),
            L('tc_reposition_09+', 'You will need to travel empty for the next pickup, Mr. Trent. Head to', R.RuleDefaultNoProcess),
            L('tc_reposition_10+', 'This delivery is complete, but the next cargo is waiting elsewhere. Your pickup base is', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_01-', 'Leave the delivered wagons here and take only the locomotive. The marker leads to your next pickup. Here are the new delivery details.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_02-', 'Travel there without the old train. Your next loaded wagons are marked at the pickup base. I will give you the shipment details now.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_03-', 'Keep the delivered train parked here. Follow the route with the locomotive alone to collect the next load. These are your new instructions.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_04-', 'The old wagons stay with their receiver. Proceed empty to the marked pickup point for your next train. Here is the new order.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_05-', 'Take just the locomotive to that base. A different train is waiting at the marker. Listen carefully to the next shipment details.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_06-', 'Do not collect the delivered wagons again. Travel empty to the new pickup marker. Dispatch will now confirm the cargo and its destination.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_07-', 'Leave this train behind and move the locomotive to the new pickup point. The next load is already assigned. Here are its delivery instructions.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_08-', 'Follow the marked route without any wagons attached. You will collect a new train there. I will now confirm what it carries and where it is going.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_09-', 'This is a move to the next loading point. Take the locomotive alone and leave the completed delivery here. The next order is as follows.', R.RuleDefaultNoProcess),
            L('tc_reposition_empty_10-', 'The receiving crew will handle the train you delivered. Head to the new marker with the locomotive only. Here are the details of the next load.', R.RuleDefaultNoProcess),
        ])
        return lines


class EngFemaleDispatcher(EnglishStationDispatcher):
    STEOS_ID = 175  # Tracer ?
    FOLDER = 'dispatcher_en02'
    IS_MALE = False
    ATTENUATION = -4


class EngFemaleRoboDispatcher(EnglishStationDispatcher):
    STEOS_ID = 175  # Tracer ?
    FOLDER = 'dispatcher_en03'
    IS_MALE = False
    ATTENUATION = -4
