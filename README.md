# Robinhood Chain Sniper 🎯
Real-time token sniper for Robinhood Chain — monitors NOXA Fun & The Odyssey.

## Features
- WebSocket live feed listener
- RobinScore: 50+ metric scoring
- Honeypot/rug detection
- Auto-buy with slippage control

```python
from src.sniper import RHCSniper
sniper = RHCSniper(min_score=70)
await sniper.listen_ws()
```
MIT © yourddy1