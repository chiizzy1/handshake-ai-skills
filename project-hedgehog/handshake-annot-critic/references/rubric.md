# Annot Critic - Calibration Examples

These examples from the onboarding assessment demonstrate the standard for precision and recall when finding AI tells.

## Example 1: Precision vs Recall
**Scenario:** Image has garbled text on many objects. One reviewer submits 2 dots (missing most). Another submits 8 dots (catching everything), but one dot is on a normal object.
**Rule:** Catching everything (recall) is crucial. An 8-dot submission is much stronger than a 2-dot one. However, false positives hurt your score: the dot on the normal object must not be marked.

## Example 2: Normal Unrequested Objects
**Scenario:** Flower shop with garbled sign text and perfectly normal, unrequested flower baskets.
**Rule:** Mark the garbled text. Do NOT mark the baskets. If the prompt didn't ask for something and didn't forbid it, extra content is not a defect.

## Example 3: Instruction Following (Spelling)
**Scenario:** Banner says "GRAND OPENNING" (prompt asked for "GRAND OPENING").
**Rule:** Note exactly what the prompt requested vs what is rendered. "The banner text is misspelled, reading 'OPENNING' with a double N instead of the requested 'OPENING'."

## Example 4: Camera Effects (Depth of Field)
**Scenario:** Duck pond with soft, low-detail water in the distance.
**Rule:** Soft water or blurry backgrounds are natural camera effects (depth of field). They are NOT AI defects and should not be marked.

## Example 5: False Positives vs Physics Defects
**Scenario:** Kitchen counter with normal apples in a bowl and water arcing horizontally sideways out of a tap.
**Rule:** Apples are plausible, normal objects (do not mark). Water arcing sideways is a physics impossibility (mark it).

## Example 6: Factuality (Real World Logic)
**Scenario:** Calendar close-up where months are out of order (March, January, November, April).
**Rule:** Check real-world logic. If months are out of order, mark it and explicitly name the wrong sequence in your note as factual proof.

## Example 7: Unrequested Characters
**Scenario:** Shopping street with an unrequested golden retriever sitting on the sidewalk.
**Rule:** Only mark the dog if the dog *itself* has an AI tell (e.g. 5 legs). If it's a perfectly normal dog, leave it alone. Do not mark things just because they weren't prompted.

## Example 8: Completely Missing Requested Elements
**Scenario:** Dining room, prompted for a large chandelier, but the ceiling is completely empty.
**Rule:** Use the text drag tool on the prompt words "a large chandelier". Do NOT drop a dot on the empty ceiling, because a dot requires a specific defect to sit on.

## Example 9: Complex Images (Scanning)
**Scenario:** Busy newsstand.
**Rule:** Scan methodically. Look for floating objects (unsupported newspaper), garbled text, impossible numbers (like 13 on a 12-hour clock face), and malformed prices (e.g., "$1.2.5"). Drop a dot directly on each one.

## Example 10: Image-wide Qualities
**Scenario:** Coastal town with uniform, unnatural graininess across the whole image.
**Rule:** Use "Overall feedback" for issues that have no single location (like global palette or extreme grain). Do not drop a point on an empty patch of sky.
